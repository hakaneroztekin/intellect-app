import os
import sys

import psycopg2 as dbapi2
import db_table_operations as tab

INIT_STATEMENTS = [
    "DROP TABLE IF EXISTS USERS", # to test changes quickly
    "DROP TABLE IF EXISTS MUSIC",
    "DROP TABLE IF EXISTS MOVIE",
    "DROP TABLE IF EXISTS MUSIC_LIST",
    "DROP TABLE IF EXISTS MOVIE_LIST",

    "CREATE TABLE IF NOT EXISTS MUSIC_LIST("
    "USER_ID INTEGER UNIQUE,"
    "MUSIC_ID INTEGER UNIQUE,"
    "PRIMARY KEY(USER_ID, MUSIC_ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS MOVIE_LIST("
    "USER_ID INTEGER UNIQUE,"
    "MOVIE_ID INTEGER UNIQUE,"
    "PRIMARY KEY(USER_ID, MOVIE_ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS USERS("
        "ID SERIAL,"
        "USERNAME VARCHAR(30) NOT NULL,"
        "NAME VARCHAR(30),"
        "SURNAME VARCHAR(30),"
        "EMAIL VARCHAR(30),"
        "PASSWORD VARCHAR(50),"
        "AGE INTEGER,"
        "GENDER VARCHAR(15),"
        "PRIMARY KEY(ID)"
#        "CONSTRAINT id_fkey_music FOREIGN KEY (ID) REFERENCES MUSIC_LIST(USER_ID)," 
#        "CONSTRAINT id_fkey_movie FOREIGN KEY (ID) REFERENCES MOVIE_LIST(USER_ID)"
    ")",
    
    "CREATE TABLE IF NOT EXISTS MUSIC("
    "ID SERIAL REFERENCES MUSIC_LIST(MUSIC_ID),"  
    "NAME VARCHAR(30),"
    "GENRE VARCHAR(30),"
    "DURATION_IN_SECONDS INTEGER,"
    "SINGER VARCHAR(30),"
    "YEAR INTEGER,"
    "PRIMARY KEY(ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS MOVIE("
    "ID SERIAL REFERENCES MOVIE_LIST(MOVIE_ID)," 
    "TITLE VARCHAR(40),"
    "YEAR INTEGER,"
    "DURATION_IN_MINUTES INTEGER,"
    "DIRECTOR VARCHAR(30),"
    "GENRE VARCHAR(30),"
    "PRIMARY KEY(ID)"
    ")",



    # user references _list's USER_ID too.

    # "INSERT INTO DUMMY VALUES (42)",
    # "   USERNAME VARCHAR(30)"
    # "   NAME VARCHAR(20)"
    # "   SURNAME VARCHAR(20)"
    # "   PASSWORD VARCHAR(100)"
    # "   AGE INTEGER"
    # "   )",
]


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
    # tab.insert_user("username", "name", "surname", "password", 70, "gender")
# jdbc:postgresql://localhost:32768/itucsdb