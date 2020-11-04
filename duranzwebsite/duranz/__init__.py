from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Somethingsecret'

from duranz import routes
