import os
import sys

import psycopg2 as dbapi2

INIT_STATEMENTS = [

#    "CREATE TABLE IF NOT EXISTS DUMMY (NUM INTEGER)",
#    "INSERT INTO DUMMY VALUES (42)",

    "CREATE TABLE IF NOT EXISTS USERS (ID INTEGER)"
    # "CREATE TABLE IF NOT EXISTS USER(ID INTEGER, USERNAME VARCHAR(30) NOT NULL, NAME VARCHAR(30), SURNAME VARCHAR(30), PASSWORD VARCHAR(50), AGE INTEGER, GENDER VARCHAR(15), PRIMARY KEY(ID))",
    # "CREATE TABLE IF NOT EXISTS MUSIC(ID INTEGER REFERENCES MUSIC_LIST(MUSIC_ID), NAME VARCHAR(30), GENRE VARCHAR(30), DURATION_IN_SECONDS INTEGER, SINGER VARCHAR(30), YEAR INTEGER, PRIMARY KEY((ID)))",
    # "CREATE TABLE IF NOT EXISTS MOVIE(ID INTEGER REFERENCES MOVIE_LIST(MOVIE_ID), TITLE VARCHAR(40), YEAR INTEGER, DURATION_IN_MINUTES INTEGER, DIRECTOR VARCHAR(30), GENRE VARCHAR(30), PRIMARY KEY(ID))",
    # "CREATE TABLE IF NOT EXISTS MUSIC_LIST(ID INTEGER, USER_ID INTEGER, MUSIC_ID INTEGER, PRIMARY KEY(ID))",
    # "CREATE TABLE IF NOT EXISTS MOVIE_LIST(ID INTEGER, USER_ID INTEGER, MOVIE_ID INTEGER, PRIMARY KEY(ID))"

    # user references _list's USER_ID too.

    # "INSERT INTO DUMMY VALUES (42)",
    # "   USERNAME VARCHAR(30)"
    # "   NAME VARCHAR(20)"
    # "   SURNAME VARCHAR(20)"
    # "   PASSWORD VARCHAR(100)"
    # "   AGE INTEGER"
    # "   )",
]
# user: id, username, name, surname, password, age, gender and music_list, movie_list as foreign keys.

def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
# jdbc:postgresql://localhost:32768/itucsdb