# Intellect app
# Upcoming Project Works:
# + Sequence I is finished
# + Sequence II is finished
#
# Sequence III
#   + Realize similar operations done on movies for music pages&lists (2 hr)
#   Improve UI (Improve UX - mobile responsibility etc.) (30 mins)
#   Test the whole system, realize same op. on Heroku (1 hr)

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_login import login_user, LoginManager

from forms import *
from config import Config
from db_table_operations import *
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

login = LoginManager(app)

from models import User, Music, Movie
@app.route("/")
def home_page():
#   tab.insert_user("username", "name", "surname", "password", 70, "gender")
    return render_template("homepage.html")


@app.route('/mylists', methods=['GET', 'POST'])
def mylists_page():
    user_movies = userlist_get_movies()
    user_musics = userlist_get_musics()
    return render_template("mylists.html",
                           user_movies=user_movies,
                           user_musics=user_musics)


@app.route('/mylists/musics', methods=['GET', 'POST'])
def musics_page():
    musics = get_musics()

    if request.method == 'POST':
        music_id = request.form['music_id']
        user_id = request.form['user_id']
        userlist_add_music(user_id, music_id)
        return redirect('/mylists/musics')

    return render_template("musics.html", musics=sorted(musics))


@app.route('/mylists/musics/add', methods=['GET', 'POST'])
def musics_add_page():
    form = MusicAddForm(request.form)
    if request.method == 'POST' and form.validate():
        music = Music(form.name.data, form.genre.data, form.duration_in_seconds.data,
                      form.singer.data, form.year.data)
        insert_music(music)
    return render_template("add_musics.html", form=form)


@app.route('/mylists/musics/update', methods=['GET', 'POST'])
def musics_update_page():
    form = MusicUpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        music = Music(form.name.data, form.genre.data, form.duration_in_seconds.data,
                      form.singer.data, form.year.data)
        music_id = form.id.data  # which music to update
        update_music(music_id, music)
        return redirect('/mylists/musics')
    return render_template("update_musics.html", form=form)
#
#
@app.route('/mylists/musics/delete', methods=['GET', 'POST'])
def musics_delete_page():
    form = MusicDeleteForm(request.form)
    id = form.music_id.data
    if id.__len__() > 0:
        delete_music(id)
        return redirect('/mylists/musics')
    return render_template("delete_musics.html", form=form)


@app.route('/mylists/movies', methods=['GET', 'POST'])
def movies_page():
    movies = get_movies()

    if request.method == 'POST':
        movie_id = request.form['movie_id']
        user_id = request.form['user_id']
        userlist_add_movie(user_id, movie_id)
        return redirect('/mylists/movies')

    return render_template("movies.html", movies= sorted(movies))

@app.route('/mylists/movies/add', methods=['GET', 'POST'])
def movies_add_page():
    form = MovieAddForm(request.form)
    if request.method == 'POST' and form.validate():
        movie = Movie(form.title.data, form.year.data, form.duration_in_minutes.data,
                      form.director.data, form.genre.data)
        insert_movie(movie)
        return redirect('/mylists/movies')
    return render_template("add_movies.html", form=form)


@app.route('/mylists/movies/update', methods=['GET', 'POST'])
def movies_update_page():
    form = MovieUpdateForm(request.form)
    if request.method == 'POST' and form.validate():
        movie = Movie(form.title.data, form.year.data, form.duration_in_minutes.data,
                      form.director.data, form.genre.data)
        movie_id = form.id.data  # which movie to update
        update_movie(movie_id, movie)
        return redirect('/mylists/movies')

    return render_template("update_movies.html", form=form)


@app.route('/mylists/movies/delete', methods=['GET', 'POST'])
def movies_delete_page():
    form = MovieDeleteForm(request.form)
    id = form.movie_id.data
    if id.__len__() > 0:
        delete_movie(id)
        return redirect('/mylists/movies')
    return render_template("delete_movies.html", form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    form = LoginForm()
    if form.validate_on_submit():
        found_user = find_user_by_username(form.username.data)
        user = User(found_user[1], found_user[2], found_user[3], found_user[4],
                    found_user[5], found_user[6], found_user[7])
        user.set_id(found_user[0]) # to load user id
        if user is None or not check_password(user.password, form.password.data):
            print("User signing failed")
            return redirect('/signin')
        login_user(user, remember=form.remember_me.data) # will be reanalyzed
        print("User signed successful")
        return redirect('/mylists')
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
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    # login_manager.login_view = 'login'
    app.run()
