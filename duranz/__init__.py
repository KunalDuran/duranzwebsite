from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Somethingsecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
db = SQLAlchemy(app)

from duranz import routes
