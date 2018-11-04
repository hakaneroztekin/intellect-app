import os
import sys

import psycopg2 as dbapi2

def insert_user(username, name, surname, password, age, gender):
    query ='INSERT INTO USERS (USERNAME, NAME, SURNAME, PASSWORD, AGE, GENDER) VALUES(%s, %s, %s, %s, %s, %s)'
    url = get_db_url()
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (username, name, surname, password, age, gender))
        # id = cursor.fetchone()[0]  # get the inserted row's id
        cursor.close()
        # return id


def get_db_url():
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    return url