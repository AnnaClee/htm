from tkinter import *
import tkinter as tk
from src.base_gui import BaseGUI

class TkinterImage(BaseGUI):
    def __init__(self, master_window, controller):
        #  calling parent constructor:
        super(TkinterImage, self).__init__(master_window, controller, "Second Frame")


        # This is for the background
        self.background_image = PhotoImage(file='bliss.png')
        self.background_label = Label(master_window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # This imports the photo, then resizes it to be three times as small
        self.photo = PhotoImage(file="facebook.png")
        self.smaller_photo = self.photo.subsample(3, 3)

        # This creates the facebook image as a button
        # This still needs a command
        self.button = Button(self, text='Facebook', image=self.smaller_photo, command=self.on_button_click).pack(side=TOP)

        # This adds another button below saying Facebook, just if they didn't click on the image
        # This still needs a command
        self.fbButton = Button(self, text='Facebook', font=(
            'Verdana', 15)).pack(pady=10, side=TOP)

    def on_button_click(self):
        # This switches to SecondFrame
        self.controller.switch_frame("login2")


if __name__ == "__main__":
    from src.controller import Controller

    # Any testing specific to this class should be done here
    window = Tk()
    app = Controller(window, TkinterImage)
    app.start()
    window.mainloop()