import os
import sys

import psycopg2 as dbapi2
import db_table_operations as tab

INIT_STATEMENTS = [
    "DROP TABLE IF EXISTS USERS CASCADE", # to test changes quickly
    "DROP TABLE IF EXISTS MUSIC CASCADE",
    "DROP TABLE IF EXISTS MOVIE CASCADE",
    "DROP TABLE IF EXISTS MUSIC_LIST CASCADE",
    "DROP TABLE IF EXISTS MOVIE_LIST CASCADE",

    "CREATE TABLE IF NOT EXISTS USERS("
        "ID SERIAL,"
        "USERNAME VARCHAR(30) NOT NULL,"
        "NAME VARCHAR(30),"
        "SURNAME VARCHAR(30),"
        "EMAIL VARCHAR(30),"
        "PASSWORD VARCHAR(100),"
        "AGE VARCHAR(8),"
        "GENDER VARCHAR(15),"
        "PRIMARY KEY(ID)"
#        "CONSTRAINT id_fkey_music FOREIGN KEY (ID) REFERENCES MUSIC_LIST(USER_ID)," 
#        "CONSTRAINT id_fkey_movie FOREIGN KEY (ID) REFERENCES MOVIE_LIST(USER_ID)"
    ")",
    
    "CREATE TABLE IF NOT EXISTS MUSIC("
    "ID SERIAL,"  
    "NAME VARCHAR(30),"
    "GENRE VARCHAR(30),"
    "DURATION_IN_SECONDS VARCHAR(8),"
    "SINGER VARCHAR(30),"
    "YEAR VARCHAR(8),"
    "PRIMARY KEY(ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS MOVIE("
    "ID SERIAL," 
    "TITLE VARCHAR(40),"
    "YEAR VARCHAR(8),"
    "DURATION_IN_MINUTES VARCHAR(8),"
    "DIRECTOR VARCHAR(30),"
    "GENRE VARCHAR(30),"
    "PRIMARY KEY(ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS MUSIC_LIST("
    "USER_ID INTEGER REFERENCES USERS(id) ON DELETE CASCADE,"
    "MUSIC_ID INTEGER REFERENCES MUSIC(id) ON DELETE CASCADE,"
    "PRIMARY KEY(USER_ID, MUSIC_ID)"
    ")",

    "CREATE TABLE IF NOT EXISTS MOVIE_LIST("
    "USER_ID INTEGER REFERENCES USERS(id) ON DELETE CASCADE,"
    "MOVIE_ID INTEGER REFERENCES MOVIE(id) ON DELETE CASCADE,"
    "PRIMARY KEY(USER_ID, MOVIE_ID)"
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