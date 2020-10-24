from tkinter import *
from functools import partial
from src.base_gui import BaseGUI
from src.bubble_start import BotBubble


class PasswordGUI(BaseGUI):
    def __init__(self, master):
        super(PasswordGUI, self).__init__(master, "User Login")

        self.label = Label(master, text="Username").grid(row=0)
        username = StringVar()
        self.username_entry = Entry(master, textvariable=username).grid(row=0, column=1)

        self.passwordLabel = Label(master, text="Password").grid(row=1, column=0)
        entered_password = StringVar()
        self.passwordEntry = Entry(master, textvariable=entered_password, show='*').grid(row=1,column=1)
        validateLogin = partial(validate_login, username, entered_password)

        self.login_button = Button(master, text="login", command=validateLogin).grid(row=4, column=0)

        self.close_button = Button(master, text="Close", command=master.quit)


def validate_login(username, entered_password):
    password = "password"
    if entered_password.get() == password:
        print("you did it!")
        a = BotBubble(canvas, message="Congratulations! You have guessed the correct password. Click NEXT SCREEN.")
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