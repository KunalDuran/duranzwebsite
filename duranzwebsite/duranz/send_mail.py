import smtplib
import os
from email.message import EmailMessage


def send_it(sub, content):

    ID = 'kunalduran11@gmail.com'# os.environ.get('MAIL_USERNAME')
    PASS = 'Kamalhogya!!' #os.environ.get('MAIL_PASS')
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = sub
    msg['From'] = ID
    msg['To'] = 'kunalduran13@gmail.com'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(ID, PASS)
        smtp.send_message(msg)

