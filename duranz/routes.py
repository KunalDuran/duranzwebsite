from flask import render_template, redirect, url_for, request
from datetime import datetime
from duranz.forms import Chatbot, WhatsappUpload, Content
from duranz.duranz_assistant import check
from duranz.whatsapp_analysis import analyze
from duranz import app, db


@app.route("/")
def home():
    time = datetime.utcnow()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('posts.html', posts=posts, time=time)


@app.route("/about")
def about():
    date = datetime.utcnow().strftime("%Y-%m-%d")
    return render_template('index.html', date=date)


@app.route('/projects')
def project():
    return render_template('project.html')


@app.route('/assistant', methods=['GET', 'POST'])
def chat():
    form = Chatbot()
    if form.validate_on_submit():
        user_query = form.query.data
        user_query = user_query.strip()
        form.response.data = check(user_query)
    return render_template('assis.html', form=form)


@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_upload():
    form = WhatsappUpload()
    if form.validate_on_submit():
        uploaded_chat = form.chat.data
        with open('uploaded_files/uploaded_chat.txt', 'wb') as file:
            file.write(uploaded_chat.read())
            analyze()
        return redirect(url_for('whatsapp_output'))
    return render_template('whatsapp_upload.html', form=form)


from duranz.models import Post
@app.route("/post", methods=['GET', 'POST'])
def new_posts():
    form = Content()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        # flash('Post added Successfully', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', form=form, legend='Write Here')


@app.route('/whatsapp_output')
def whatsapp_output():
    return render_template('whatsapp.html')
