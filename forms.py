from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    BooleanField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=6, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    email = StringField('Email Address', validators=[Length(min=8, max=35), Email()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')