from src.base_gui import BaseGUI
from tkinter import *
from src.controller import Controller
from src.login import PasswordGUI


# from tkinter import *
# import tkinter as tk

# from PIL import Image, ImageTK

# root = tk.Tk()
# root.geometry("1054x576")
#
# #This is for the background
# background_image = tk.PhotoImage(file='bliss.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0,y=0, relwidth=1, relheight=1)
#
# #This imports the photo, then resizes it to be three times as small
# photo = PhotoImage(file="facebook.png")
# smaller_photo = photo.subsample(3, 3)
#
# #This creates the facebook image as a button
# #This still needs a command
# Button(root, text = 'Facebook', image=smaller_photo).pack(side=TOP)
#
# #This adds another button below saying Facebook, just if they didn't click on the image
# #This still needs a command
# fbButton = Button(root, text = 'Facebook', font =(
#   'Verdana', 15)).pack(pady = 10, side=TOP)

class TkinterImage(BaseGUI):
    def __init__(self, master_window, controller):
        #  calling parent constructor:
        super(TkinterImage, self).__init__(master_window, controller, "Second Frame")

        # This is for the background
        self.background_image = PhotoImage(file='bliss.png')
        self.background_label = Label(self, image=self.background_image)
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
        self.controller.switch_frame(PasswordGUI)



if __name__ == "__main__":
    # Any testing specific to this class should be done here
    window = Tk()
    app = Controller(window, TkinterImage)
    app.start()
    window.mainloop()
