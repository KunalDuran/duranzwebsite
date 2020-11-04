from flask import render_template, redirect, url_for, request, flash
from duranz.forms import ProjectRequestForm
from duranz import app
from duranz.send_mail import send_it


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/projects')
def project():
    return render_template('project.html', title='Projects by Kunal')


@app.route('/services')
def services():
    return render_template('services.html', title='Services at Duranz')


@app.route('/query_form', methods=['GET', 'POST'])
def query_form():
    form = ProjectRequestForm()
    if form.validate_on_submit():
        subject = form.project.data
        body = '  =====   '.join([ form.name.data, form.email.data, form.project.data, form.detail.data])
        send_it(subject, body)
        mailed(form.email.data)
        return redirect(url_for('home'))
    else:
        print("something went wrong")
    return render_template('query_form.html', form=form, title='Request Service')


def mailed(recipients):
    msg = Message('Repair Request Accepted', recipients=[recipients])
    msg.body = ''' Thanks for using our service. Keep in touch with us on our whatsapp number '''
    mail.send(msg)

