from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    BooleanField, SelectField, IntegerField,
    SubmitField, TextAreaField)
from wtforms.validators import (
    DataRequired, Length, EqualTo,
    Email, InputRequired)


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(),
                                Length(min=4, max=20)])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=20),
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
    recipe_name = StringField(
        'Recipe Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField(
        'Recipe Description', validators=[DataRequired(), Length(max=100)])
    prep_time = StringField(
        'Prep Time (minutes)', validators=[DataRequired(), Length(max=3)])
    cook_time = StringField(
        'Cook Time (minutes)', validators=[DataRequired(), Length(max=3)])
    serves = SelectField(
        '', choices=[(None, "Servings (choose an option)"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
        validate_choice=True, validators=[DataRequired()])
    difficulty = SelectField(
        '', choices=[(None, "Difficulty (choose an option)"), ("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")], validate_choice=True, validators=[DataRequired()])
    tags = StringField(
        'Tags (separate each with a comma)', validators=[DataRequired()])
    image = StringField('Image link', validators=[DataRequired()])
    ingredients = TextAreaField(
        'Ingredients (one per line)', validators=[DataRequired()])
    method = TextAreaField(
        'Method (one step per line)', validators=[DataRequired()])
    submit = SubmitField('Add Recipe')


class EditRecipeForm(FlaskForm):
    recipe_name = StringField(
        'Recipe Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField(
        'Recipe Description', validators=[DataRequired(), Length(max=100)])
    prep_time = StringField(
        'Prep Time (minutes)', validators=[DataRequired(), Length(max=3)])
    cook_time = StringField(
        'Cook Time (minutes)', validators=[DataRequired(), Length(max=3)])
    serves = SelectField(
        '', choices=[(None, "Servings (choose an option)"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
        validate_choice=True, validators=[DataRequired()])
    difficulty = SelectField(
        '', choices=[(None, "Difficulty (choose an option)"), ("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")], validators=[DataRequired()])
    tags = StringField(
        'Tags (separate each with a comma)', validators=[DataRequired()])
    image = StringField('Image link', validators=[DataRequired()])
    ingredients = TextAreaField(
        'Ingredients (one per line)', validators=[DataRequired()])
    method = TextAreaField('Method', validators=[DataRequired()])
    submit = SubmitField('Update Recipe')


class ConfirmDelete(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    submit = SubmitField('Delete Recipe')
