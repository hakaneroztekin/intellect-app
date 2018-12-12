from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms import validators, Form

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=30)])
    email = StringField('Email Address', [validators.Length(min=4, max=30)])
    name = StringField('Name', [validators.Length(min=0, max=20)])
    surname = StringField('Surname', [validators.Length(min=0, max=20)])
    age = StringField('Age', [validators.Length(min=0, max=20)])
    gender = StringField('Gender', [validators.Length(min=0, max=15)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class MovieAddForm(Form):
    title = StringField('Title', [validators.Length(min=3, max=30)])
    year = StringField('Year', [validators.Length(min=4, max=30)])
    duration_in_minutes = StringField('Duration', [validators.Length(min=0, max=20)])
    director = StringField('Director', [validators.Length(min=0, max=20)])
    genre = StringField('Genre', [validators.Length(min=0, max=20)])


{#     Music DB Model   #}
{#    "NAME VARCHAR(30),"#}
{#    "GENRE VARCHAR(30),"#}
{#    "DURATION_IN_SECONDS VARCHAR(8),"#}
{#    "SINGER VARCHAR(30),"#}
{#    "YEAR VARCHAR(8),"#}

class MusicAddForm(Form):
    name = StringField('Name', [validators.Length(min=3, max=30)])
    genre = StringField('Genre', [validators.Length(min=4, max=30)])
    duration_in_seconds = StringField('Duration(seconds)', [validators.Length(min=0, max=20)])
    singer = StringField('Singer', [validators.Length(min=0, max=20)])
    year = StringField('Year', [validators.Length(min=0, max=20)])