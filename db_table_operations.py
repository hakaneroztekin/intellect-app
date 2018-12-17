from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys
import psycopg2 as dbapi2

# USER AUTHENTICATION TABLE OPERATIONS #
def insert_user(object):
    query ='INSERT INTO USERS (USERNAME, NAME, SURNAME, EMAIL, PASSWORD, AGE, GENDER) ' \
           'VALUES(%s, %s, %s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        # hash the password
        print("User pw:" + object.password)
        password_hash = generate_password_hash(object.password)
        print("User pw:" + password_hash)
        cursor.execute(query, (object.username, object.name, object.surname, object.email,
                               password_hash, object.age, object.gender))
        # print("User pw:" + object.password.decode("utf-8"))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()


def find_user_by_username(username):
    query = "SELECT * FROM USERS WHERE USERNAME = %s"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        rows_count = cursor.execute(query,(username,))
        print("User is found in DB")
        found_user = cursor.fetchone()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return found_user


def find_user_by_id(id):
    query = "SELECT * FROM USERS WHERE ID = %s"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        rows_count = cursor.execute(query,(id,))
        print("User is found in DB")
        found_user = cursor.fetchone()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return found_user


def check_password(user_password_hash, form_password):
    # compare the passwords
    return check_password_hash(user_password_hash, form_password)

# USER LIST OPERATIONS
def userlist_add_movie(user_id, movie_id):
    query = 'INSERT INTO MOVIE_LIST (USER_ID, MOVIE_ID) VALUES(%s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (user_id, movie_id))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id
def userlist_get_movies():
    query ='SELECT MOVIE.* FROM MOVIE_LIST ' \
           'INNER JOIN MOVIE ON MOVIE_LIST.MOVIE_ID = MOVIE.ID ' \
           'INNER JOIN USERS ON MOVIE_LIST.USER_ID = USERS.ID'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        movies = cursor.fetchall()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return movies
        # return id

# MUSIC TABLE OPERATIONS #
def get_musics():
    query ='SELECT * FROM MUSIC'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        movies = cursor.fetchall()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return movies
        # return id


def insert_music(music):
    query ='INSERT INTO MUSIC (NAME, GENRE, DURATION_IN_SECONDS, SINGER, YEAR) VALUES(%s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (music.name, music.genre, music.duration_in_seconds,
                               music.singer, music.year))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id


def update_music(music_id, music):
    query = "UPDATE MUSIC " \
            "SET NAME = %s, " \
            "GENRE = %s, " \
            "DURATION_IN_SECONDS = %s, " \
            "SINGER = %s, " \
            "YEAR = %s " \
            "WHERE ID = %s "
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (music.name, music.genre, music.duration_in_seconds,
                               music.singer, music.year, music_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("Music with id " + music_id + " deleted")
        # return id
        
def delete_music(music_id):
    query = "DELETE FROM MUSIC WHERE ID = CAST(%s AS INTEGER)"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (music_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("Music with id " + music_id + " deleted")
        # return id

# MOVIE TABLE OPERATIONS #
def get_movies():
    query ='SELECT * FROM MOVIE'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        movies = cursor.fetchall()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return movies
        # return id


def insert_movie(movie):
    query ='INSERT INTO MOVIE(TITLE, YEAR, DURATION_IN_MINUTES, DIRECTOR, GENRE) VALUES(%s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (movie.title, movie.year, movie.duration_in_minutes, movie.director, movie.genre))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id

def update_movie(movie_id, movie):
    query = "UPDATE MOVIE " \
            "SET TITLE = %s, " \
            "YEAR = %s, " \
            "DURATION_IN_MINUTES = %s, " \
            "DIRECTOR = %s, " \
            "GENRE = %s " \
            "WHERE ID = %s "
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (movie.title, movie.year, movie.duration_in_minutes,
                              movie.director, movie.genre, movie_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("Movie with id " + movie_id + " deleted")
        # return id


def delete_movie(movie_id):
    query = "DELETE FROM MOVIE WHERE ID = CAST(%s AS INTEGER)"
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (movie_id,))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        print("Movie with id " + movie_id + " deleted")
        # return id

        
def get_db_url():
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    return url