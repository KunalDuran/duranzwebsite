from flask import render_template, redirect, url_for, request, flash
from duranz.forms import ProjectRequestForm
from duranz import app


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
        pass
    return render_template('query_form.html', form=form, title='Request Service')


