from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Somethingsecret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
#db = SQLAlchemy(app)

from duranz import routes
