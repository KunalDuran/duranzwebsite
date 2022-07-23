from flask import render_template, flash, request
from duranz import app

import requests


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/projects')
def project():
    return render_template('project.html', title='Projects by Kunal')


@app.route('/playerstats', methods=['GET', 'POST'])
def playerstats():
    if request.method == 'POST':
        flash('Your Query is Sent', 'success')

        form_data = request.form.to_dict()
        print(form_data)

        url = f"http://api.kunalduran.com/player-stats/{form_data['player']}?format={form_data['format']}&season={form_data['season']}"
        response = requests.get(url).json()
        print(response)
        output=response['content'][0]
        return  render_template('query_form.html', output=output, title='Player Stats')
    return render_template('query_form.html', title='Player Stats')


@app.route('/about')
def about():
    return render_template('about.html', title='About Duranz')


@app.route('/wkguide')
def wkguide():
    return render_template('comprehensiveWK.html', title='Comprehensive WK Guide')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404