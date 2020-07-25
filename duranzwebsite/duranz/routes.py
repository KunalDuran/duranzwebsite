from flask import render_template, redirect, url_for, request, flash
from datetime import datetime
from duranz.forms import Chatbot, WhatsappUpload, Content, RepairRequestForm
from duranz.duranz_assistant import  total_preprocessing
from duranz.whatsapp_analysis import analyze
from duranz import app
#import mysql.connector 
from duranz.send_mail import send_it
import pymysql
import os


db_user = 'root'
db_password = 'HathLagaKDikha'
db_name = 'pehla'
db_connection_name = 'duranzwebsite:asia-south1:duranzwebsitesdb'


def sql_check():
    if os.environ.get('GAE_ENV') == 'standard':
        # If deployed, use the local socket interface for accessing Cloud SQL
        unix_socket = '/cloudsql/{}'.format(db_connection_name)
        conn = pymysql.connect(user=db_user, password=db_password,
                              unix_socket=unix_socket, db=db_name)
    else:
        # If running locally, use the TCP connections instead
        # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
        # so that your application can use 127.0.0.1:3306 to connect to your
        # Cloud SQL instance
        host = '127.0.0.1'
        conn = pymysql.connect(user=db_user, password=db_password,
                              host=host, db=db_name, port=3307)

    c = conn.cursor()

    return conn, c
        
    
#def sql_check():
#    #conn = mysql.connector.connect(host="localhost", user="root", passwd="password", database="pehla")
#    #cursor = conn.cursor()
#    conn = pymysql.connect(host='127.0.0.1',
#                             user=db_user,
#                             password=db_password,
#                             db='pehla',port=3307)
#    cursor = conn.cursor()
#    return conn, cursor
    

@app.route("/")
def home():
    conn, c = sql_check()    
    c.execute("SELECT * FROM blogs LIMIT 5")
    article = list(c)
    conn.close()
    time = datetime.utcnow().strftime("%Y-%m-%d")
    return render_template('index.html', time=time,  article=article)


@app.route("/about")
def about():
    date = datetime.utcnow().strftime("%Y-%m-%d")
    return render_template('about.html', date=date, title='About Kunal')


@app.route('/projects')
def project():
    return render_template('project.html', title='Projects by Kunal')


@app.route('/assistant', methods=['GET', 'POST'])
def chat():
    form = Chatbot()
    if form.validate_on_submit():
        user_query = form.query.data
        user_query = user_query.strip()
        processed_query = total_preprocessing(user_query, 20)
        print(processed_query)
        return render_template('assis.html', form=form, processed_query=processed_query)
#form.response.data = check(user_query)
    return render_template('assis.html', form=form, title='Duranz Assistant')


@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_upload():
    form = WhatsappUpload()
    if form.validate_on_submit():
        uploaded_chat = form.chat.data
        with open('uploaded_files/uploaded_chat.txt', 'wb') as file:
            file.write(uploaded_chat.read())
            analyze()
        return redirect(url_for('whatsapp_output'))
    return render_template('whatsapp_upload.html', form=form, title='Awesome Whatsapp Analysis')


#from duranz.models import Post
@app.route("/new_post", methods=['GET', 'POST'])
def new_posts():
    form = Content()
    if form.validate_on_submit():
        conn, c = sql_check() 
        title = form.title.data
        content = form.content.data
        time = datetime.utcnow().strftime("%Y-%m-%d")
        c.execute("INSERT INTO blogs(title, content, time) VALUES (%s,%s,%s)", (title, content, time))
        conn.commit()
        conn.close()
        # flash('Post added Successfully', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', form=form, legend='Write Here', title='Create Post')


@app.route('/whatsapp_output')
def whatsapp_output():
    return render_template('whatsapp.html', title='Whatsapp WordCloud')


@app.route('/post/<int:post_id>')
def post(post_id):
    conn, c = sql_check()
    c.execute("SELECT * FROM blogs WHERE id={}".format(post_id))
    post = list(c)
    return render_template('post.html', post=post, title=post[0][1])


@app.route('/post/<int:post_id>/update', methods=['GET','POST'])
def update_post(post_id):
    conn, c = sql_check()
    c.execute("SELECT * FROM blogs WHERE id={}".format(post_id))
    post = list(c)
    conn.close()
    form = Content()

    if form.validate_on_submit():
        conn, c = sql_check()
        c.execute('''UPDATE blogs SET title='{}', content='{}' WHERE id={}'''.format(form.title.data, form.content.data, post_id))
        conn.commit()
        conn.close()
        flash('Post Updated Successfully', 'success')
        return  redirect(url_for('home'))
    elif request.method == "GET":
        form.title.data = post[0][1]
        form.content.data = post[0][2]
    return render_template('update_post.html', form=form, legend='Update Post', title='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    conn, c = sql_check()
    c.execute('''DELETE FROM blogs WHERE id={}'''.format(post_id))
    conn.commit()
    conn.close()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
    
    
    
@app.route("/all_posts")
def all_posts():
    conn, c = sql_check()    
    c.execute("SELECT * FROM blogs")
    article = list(c)
    print(article)
    conn.close()
    time = datetime.utcnow().strftime("%Y-%m-%d")
    return render_template('all_posts.html', time=time,  article=article)
    
    
def mailed(recipients):
    msg = Message('Repair Request Accepted', recipients=[recipients])
    msg.body = ''' Thanks for using our service. Keep in touch with us on our whatsapp number '''
    mail.send(msg)


@app.route("/services", methods=['GET', 'POST'])
def services():
    form = RepairRequestForm()
    if form.validate_on_submit():
        subject = form.product.data
        body = '  =====   '.join([form.detail.data, form.address.data, form.email.data])
        send_it(subject, body)
        mailed(form.email.data)
        return redirect(url_for('home'))
    return render_template('service.html', form=form)
    

