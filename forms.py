from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    BooleanField, SelectField, IntegerField,
    SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(),
                                Length(min=4, max=20)])
    password = PasswordField(
        'Password', validators=[DataRequired(),
                                EqualTo(
                                    'password2',
                                    message='Passwords do not match, please try again')])
    password2 = PasswordField('Repeat Password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class AddRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    recipe_description = TextAreaField(
        'Recipe Description', validators=[DataRequired()])
    prep_time = IntegerField('Prep Time', validators=[DataRequired()])
    cook_time = IntegerField('Cook Time', validators=[DataRequired()])
    serves = SelectField(
        'Servings (choose an option)', choices=[(2), (4), (6), (8), (10)],
        validate_choice=True, validators=[DataRequired()])
    difficulty = SelectField(
        'Difficulty (choose an option)',
        choices=[('Easy'), ('Medium'), ('Hard')], validators=[DataRequired()])
    tags = StringField(
        'Tags (separate each with a comma', validators=[DataRequired()])
    image = StringField('Image link', validators=[DataRequired()])
    ingredients = TextAreaField(
        'Ingredients (one per line)', validators=[DataRequired()])
    method = TextAreaField('Method', validators=[DataRequired()])

