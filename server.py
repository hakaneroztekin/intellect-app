# Intellect app
# Last 3 Works Done
# (06.11.18) A successful signup operation: Front-end variables (Form) -> Models methods -> Database record
# (07.11.18) Fix Heroku App crash
# (5.12.18)  Fix find user SQL for user sign in.
#
# Upcoming Project Works:
# Sequence I (Remaining)
#   Sign-in operation (Authentication) (2-4 hrs.) -> 1 hr left
#   > Add check_password in for sign-in
#   > (optionally) You can show logged user in front-end
#
# Sequence II
#   Fix Foreign keys (1-1,5 hr)
#   Movies, Musics form and buttons (MyLists Page /Frontend) (2 hrs)
#   Related database operations (/Backend) (2 hrs)
# Sequence III
#   Improve UI (1 hr)
#   Wrap-up, and Heroku tests (1 hr)
#   Documentation, presentation (2-4 hrs)

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_login import login_user

from forms import LoginForm, RegistrationForm
from config import Config
from models import User, Music, Movie
from db_table_operations import *

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
    if form.validate_on_submit():
        user = find_user_by_username(form.username.data)
        if user != 0: # if user is found
            if user is None or not user.check_password(form.password.data):
                return redirect('/signin')
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
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
