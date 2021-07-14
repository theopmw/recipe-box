from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    BooleanField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(),
                                Length(min=4, max=20)])
    password = PasswordField(
        'Password', validators=[DataRequired(),
                                EqualTo('password2', message='Passwords do not match, please try again')])
    password2 = PasswordField('Repeat Password')
    submit = SubmitField('Register')
