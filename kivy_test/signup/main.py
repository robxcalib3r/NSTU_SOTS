# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from userdb import UserDB
from busdb import  BusDB


class SignUpWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") and self.role.text != "Select your Role":
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text, self.role.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        self.role.text = "Select Your Role"

    def role_spinner_clicked(self, value):
        pass


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self, *args):
        if db.validate(self.email.text, self.password.text):
            ProfileWindow.current = self.email.text
            self.reset()
            sm.current = "lain"

        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class ProfileWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""


    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, role, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.role.text = "Role: " + role
        self.created.text = "Created On: " + created



class MainWindow(Screen):
    toLogin = ObjectProperty(None)
    label_text = StringProperty('')

    def onClick(self):
        devPhase()

    def on_enter(self, *args):
        self.ids.toLogin.text = db.get_user(ProfileWindow.current)[1]


class busSched(Screen):
    def showData(self):
        pass
    def on_enter(self, *args):
        maijtime, camtime = db1.getFreq()
        print(maijtime)
        print(camtime)
        self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))
        for data in camtime:
            lbl = Button(text=data + "          Students: " + str(camtime.get(data)) + "          Buses: ")
            self.ids.scroll.add_widget(lbl)


        self.ids.scroll1.bind(minimum_height=self.ids.scroll1.setter('height'))
        for data in maijtime:
            lbl = Button(text=data + "          Students: " + str(maijtime.get(data)) + "          Buses: ")
            self.ids.scroll1.add_widget(lbl)

class PersonalEntry(Screen):
    def submit(self):
        if self.ids.time_select_versity.text != "Select Time" and self.ids.time_select_maijdee.text != "Select Time":
                db1.addDataPerson(ProfileWindow.current, self.ids.time_select_maijdee.text, self.ids.time_select_versity.text, "Maijdee", "Campus")


                self.ids.submit_time.text = "Submission Completed"
        else:
            invalidForm()



class classEntry(Screen):
    def onClick(self):
        devPhase()

class busLocate(Screen):
    def onClick(self):
        devPhase()

class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()

def devPhase():
    pop = Popup(title='Sorry, This page is still in active development',
                content=Label(text='The Developer is trying his best to provide you\n'
                                   ' all with the Best NSTU transportation service'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file("my.kv")
db = UserDB("users.txt")
db1 = BusDB("busSched.txt")

print(db.get_user("robin@email.com"))
sm = WindowManager()

screens = [LoginWindow(name="login"), SignUpWindow(name="create"), ProfileWindow(name="profile"),
           MainWindow(name="lain"), busSched(name="busSched"), PersonalEntry(name="pEntry"),
           classEntry(name="cEntry"), busLocate(name="busLocate")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
