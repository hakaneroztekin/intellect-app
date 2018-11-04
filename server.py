# Intellect app
#
# Upcoming Project Works:
# Views
# Database configuration & connection testing (as announced in the original repo, itucsdb1809)
# Database methods (INSERT INTO etc.)
# Signup form (with DB actions)
# Signin form
# Authentication
# Logout action
# Movies, Musics form and its actions (adding, updating musics etc.)
# Report, Presentation

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home_page():
    print(os.environ)
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
