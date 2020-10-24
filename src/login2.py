from tkinter import *
from functools import partial
from src.base_gui import BaseGUI



class PasswordGUI2(BaseGUI):
    def __init__(self, master, controller):
        super(PasswordGUI2, self).__init__(master,controller, "User Login")

        self.label = Label(master, text="Username").grid(row=0,column=1)
        username = StringVar()
        self.username_entry = Entry(master, textvariable=username).grid(row=0, column=2)

        self.passwordLabel = Label(master, text="Password").grid(row=1, column=1)
        entered_password = StringVar()
        self.passwordEntry = Entry(master, textvariable=entered_password, show='*').grid(row=1,column=2)
        validateLogin = partial(self.validate_login, username, entered_password)

        self.login_button = Button(master, text="login", command=validateLogin).grid(row=4, column=0)

        self.close_button = Button(master, text="Close", command=master.quit)


    def validate_login(self, username, entered_password):
        password = "remember"
        if entered_password.get() == password:
            self.controller.switch_frame('chat3')
        else:
            self.controller.switch_frame('Phishing')


if __name__ == "__main__":
    root = Tk()
    root.config(bg="white")
    canvas = Canvas(root, width=1024, height=576, bg="white")
    canvas.grid(row=0, column=0, columnspan=3)
