# userdb.py

import datetime


class UserDB:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()


    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}
        emails = ""

        for line in self.file:
            email, password, name, role, created = line.strip().split(";")
            self.users[email] = (password, name, role, created)

        return self.users
        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def get_email(self):
        pass

    def add_user(self, email, password, name, role):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), role.strip(), UserDB.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + ";" + self.users[user][3] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]