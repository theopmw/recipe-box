from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    BooleanField, SelectField, IntegerField,
    SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length, EqualTo, Email, InputRequired


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


class CreateRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    description = TextAreaField(
        'Recipe Description', validators=[DataRequired()])
    prep_time = StringField('Prep Time (minutes)', validators=[DataRequired()])
    cook_time = StringField('Cook Time (minutes)', validators=[DataRequired()])
    serves = SelectField(
        '', choices=[(None, "Servings (choose an option)"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
        validate_choice=True, validators=[DataRequired()])
    difficulty = SelectField(
        '', choices=[(None, "Difficulty (choose an option)"), ("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")], validators=[DataRequired()])
    tags = StringField(
        'Tags (separate each with a comma)', validators=[DataRequired()])
    image = StringField('Image link', validators=[DataRequired()])
    ingredients = TextAreaField(
        'Ingredients (one per line)', validators=[DataRequired()])
    method = TextAreaField('Method', validators=[DataRequired()])
    submit = SubmitField('Add Recipe')


class EditRecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    description = TextAreaField(
        'Recipe Description', validators=[DataRequired()])
    prep_time = StringField('Prep Time (minutes)', validators=[DataRequired()])
    cook_time = StringField('Cook Time (minutes)', validators=[DataRequired()])
    serves = SelectField(
        '', choices=[(None, "Servings (choose an option)"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
        validate_choice=True, validators=[DataRequired()])
    difficulty = SelectField(
        '', choices=[(None, "Difficulty (choose an option)"), ("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")], validators=[DataRequired()])
    tags = StringField(
        'Tags (separate each with a comma)', validators=[DataRequired()])
    image = StringField('Image link', validators=[DataRequired()])
    ingredients = TextAreaField(
        'Ingredients (one per line)', validators=[DataRequired()])
    method = TextAreaField('Method', validators=[DataRequired()])
    submit = SubmitField('Update Recipe')
