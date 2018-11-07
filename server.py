# Intellect app
# Last 3 Works Done
# (04.10.18) Database configuration, connection, Docker installation, initialization and insert statements
# (06.10.18) A successful signup operation: Front-end variables (Form) -> Models methods -> Database record
# (07.10.18) Fix Heroku App crash
#
# Upcoming Project Works:
# Sequence I (Remaining)
#   Improving models.py and its methods
#   Sign-in operation (Authentication)
# Sequence II
#   Fix Foreign keys
#   Movies, Musics form and buttons (MyLists Page /Frontend)
#   Related database operations (/Backend)
# Sequence III
#   Wrap-up and Heroku tests
#   Documentation, presentation

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from forms import LoginForm, RegistrationForm
import os
import db_table_operations as tab
from config import Config
from models import User, Music, Movie
from db_table_operations import insert_user, insert_movie, insert_music

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)


@app.route("/")
def home_page():
#   tab.insert_user("username", "name", "surname", "password", 70, "gender")
    return render_template("homepage.html")


@app.route('/mylists')
def mylists_page():
    return render_template("mylists.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    form = LoginForm()
    return render_template("signin.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.name.data, form.surname.data, form.email.data,
                    form.password.data, form.age.data, form.gender.data)
        insert_user(user)
    return render_template("signup.html", form=form)

if __name__ == "__main__":
    app.run()
