from tkinter import *
import tkinter as tk
from src.base_gui import BaseGUI

class Phishing(BaseGUI):
    def __init__(self, master_window, controller):
        #  calling parent constructor:
        super(Phishing, self).__init__(master_window, controller, "Third Frame")


        # This is for the background
        self.background_image = PhotoImage(file='phishing.png')
        self.background_label = Label(master_window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # This adds another button below saying Facebook, just if they didn't click on the image
        # This still needs a command
        self.aButton = Button(self, text='A', font=(
            'Verdana', 15), command=self.on_button_click).pack(side=TOP)
        self.bButton = Button(self, text='B', font=(
            'Verdana', 15), command=self.on_button_click).pack(side=TOP)
        self.cbButton = Button(self, text='C', font=(
            'Verdana', 15), command=self.on_button_click).pack(side=TOP)

    def on_button_click(self):
        # This switches to SecondFrame
        self.controller.switch_frame('chat3')


if __name__ == "__main__":
    from src.controller import Controller

    # Any testing specific to this class should be done here
    window = Tk()
    app = Controller(window, Phishing)
    app.start()
    window.mainloop()