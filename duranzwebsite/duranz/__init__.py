from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Somethingsecret'
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL= True,
    MAIL_USERNAME = 'kunalduran11@gmail.com',
    MAIL_PASSWORD = 'Kamalhogya!!'

)

mail = Mail(app)
from duranz import routes
