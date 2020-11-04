from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField,  SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
    
    
class ProjectRequestForm(FlaskForm):
    name = StringField('Enter Your/Company Name', validators=[DataRequired()])
    email = StringField('Enter Email ID', validators=[Email(), DataRequired()])
    project = StringField('Type of Project', validators=[DataRequired()])
    detail = TextAreaField('Details of the Project', validators=[DataRequired()])
    sample_file = FileField('Upload Sample Files')
    submit = SubmitField('Request')

