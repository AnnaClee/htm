from tkinter import *
import tkinter as tk
#from PIL import Image, ImageTK

root = tk.Tk()
root.geometry("1054x576")

#This is for the background
background_image = tk.PhotoImage(file='bliss.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

#This imports the photo, then resizes it to be three times as small
photo = PhotoImage(file="facebook.png")
smaller_photo = photo.subsample(3, 3)

#This creates the facebook image as a button
#This still needs a command
Button(root, text = 'Facebook', image=smaller_photo).pack(side=TOP)

#This adds another button below saying Facebook, just if they didn't click on the image
#This still needs a command
fbButton = Button(root, text = 'Facebook', font =(
  'Verdana', 15)).pack(pady = 10, side=TOP)







root.mainloop()