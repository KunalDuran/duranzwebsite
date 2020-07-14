from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField,  SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class Chatbot(FlaskForm):
    query = TextAreaField('Type Here', validators=[DataRequired()])
    response = TextAreaField('Duranz Assistant Response')
    submit = SubmitField('Ask')


class WhatsappUpload(FlaskForm):
    chat = FileField('Upload file', validators=[FileAllowed(['txt'])])
    submit = SubmitField('Upload chats')


# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=30)])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')


class Content(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
