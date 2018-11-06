

class User():
    def __init__(self, username, name, surname, email, password, age, gender):
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password.encode()
        self.age = int(age)
        self.gender = gender
        print("User model object created")


class Music():
    def __init__(self):
        print("I am a music.")


class Movie():
    def __init__(self):
        print("I am a movie.")