import os
import sys
import psycopg2 as dbapi2

# USER TABLE OPERATIONS #
def insert_user(object):
    query ='INSERT INTO USERS (USERNAME, NAME, SURNAME, EMAIL, PASSWORD, AGE, GENDER) ' \
           'VALUES(%s, %s, %s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (object.username, object.name, object.surname, object.email,
                               object.password, object.age, object.gender))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()

def find_user_by_username(username):
    query ='SELECT * FROM USERS WHERE(USERNAME = USERNAME) VALUES(%s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, username)
        found_user = cursor.fetchone()
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        return found_user


# MUSIC TABLE OPERATIONS #
def insert_music(name, genre, duration_in_seconds, singer, year):
    query ='INSERT INTO MUSIC (NAME, GENRE, DURATION_IN_SECONDS, SINGER, YEAR) VALUES(%s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (name, genre, duration_in_seconds, singer, year))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id

# MOVIE TABLE OPERATIONS #
def insert_movie(title, year, duration_in_minutes, director, genre):
    query ='INSERT INTO MOVIE(TITLE, YEAR, DURATION_IN_MINUTES, DIRECTOR, GENRE) VALUES(%s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (title, year, duration_in_minutes, director, genre))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id

        
def get_db_url():
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    return url