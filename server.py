# Intellect app
# (04.10.18) Database configuration, connection, Docker installation, initialization and insert statements
#
# Upcoming Project Works:
# Sequence I
#   A successful signup operation: Front-end variables (Form) -> Models methods -> Database record
#   Improving models.py
#   Sign-in operation (Authentication)
# Sequence II
#   Movies, Musics form and its actions (add, delete)
# Sequence III
#   Wrap-up and Heroku tests
#   Documentation, presentation

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
import db_table_operations as tab

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home_page():
    print(os.environ)
    tab.insert_user("username", "name", "surname", "password", 70, "gender")
    return render_template("homepage.html")


@app.route('/mylists')
def mylists_page():
    return render_template("mylists.html")


@app.route('/signin')
def signin_page():
    return render_template("signin.html")


@app.route('/signup')
def signup_page():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run()
