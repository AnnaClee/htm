from tkinter import *
from functools import partial
from src.base_gui import BaseGUI



class PasswordGUI(BaseGUI):
    def __init__(self, master, controller):
        super(PasswordGUI, self).__init__(master, controller, "User Login")

        self.label = Label(self, text="Username").grid(row=0, column=1)
        username = StringVar()
        self.username_entry = Entry(self, textvariable=username).grid(row=0, column=2)

        self.passwordLabel = Label(self, text="Password").grid(row=1, column=1)
        entered_password = StringVar()
        self.passwordEntry = Entry(self, textvariable=entered_password, show='*').grid(row=1, column=2)
        validateLogin = partial(self.validate_login, username, entered_password)

        self.login_button = Button(self, text="login", command=validateLogin).grid(row=4, column=1)

        self.close_button = Button(self, text="Close", command=self.quit)


    def validate_login(self, username, entered_password):
        password = "password"
        if entered_password.get() == password:
            self.controller.switch_frame('chat2')
        else:
            print("incorrect password")


if __name__ == "__main__":
    root = Tk()
    root.config(bg="white")
    canvas = Canvas(root, width=1024, height=576, bg="white")
    canvas.grid(row=0, column=0, columnspan=3)

    # Any testing specific to this class should be done here
    window1 = Tk()  # initialize the window manager with the tkinter.Tk() method and assign it to a variable
    PasswordGUI(window1)
    window1.mainloop()