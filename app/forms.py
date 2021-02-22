from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, TextField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    # Enable CSRF
    # csrf = True  
    # csrf_class = SomeCSRF  
    # csrf_secret = b'myform' 

    #initializing form fields
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    subject = TextField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])

