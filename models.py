from flask_login import UserMixin
from db_table_operations import find_user_by_id, find_user_by_username

def initialize_login():
    from server import login
    global login
    login = login


class User(UserMixin):
    initialize_login()

    def __init__(self, username, name, surname, email, password, age, gender):
        self.id = 0
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.age = int(age)
        self.gender = gender
        print("User object created")

    @login.user_loader
    def load_user(id): # burda sorun var, id=0 yolluyor hep, init'te verdiğim değeri yani.
        if id == 0:
            print("User not logged in, id is ", id)
            return
        else:
            found_user = find_user_by_id(int(id))
            print("found user username: ", found_user)
            return found_user

    def __repr__(self):
        return '<User %r>' % self.username

    def set_id(self, id): # grab row ID and set it as user object ID
        #user = find_user_by_username(self.username)
        #self.id = user[0]  # user[0] is user ID
        self.id = id

    def get_id(self):
        return self.id;

class Music:
    def __init__(self, name, genre, duration_in_seconds, singer, year):
        self.name= name
        self.genre = genre
        self.duration_in_seconds = duration_in_seconds
        self.singer = singer
        self.year = year
        print("Music object created")


class Movie:
    def __init__(self, title, year, duration_in_minutes, director, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.duration_in_minutes = duration_in_minutes
        self.director = director
        print("Movie object created")