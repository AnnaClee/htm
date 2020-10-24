from tkinter import *
from datetime import datetime
import textwrap


root = Tk()
root.config(bg="white")

canvas = Canvas(root, width=1024, height=576,bg="white")
canvas.grid(row=0,column=0,columnspan=3)

bubbles = []
messages = ["Hello and welcome to our internet safety game! Click CONTINUE to proceed.",
            "I am here to explain how things will work.",
            "Firstly we ask you to login by typing a password to enter with the username shown. Click NEXT SCREEN to advance screens."]

class BotBubble():
    def __init__(self,master,message=""):
        self.master = master
        self.frame = Frame(master,bg="salmon")
        self.i = self.master.create_window(90,400,window=self.frame)
        Label(self.frame,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="salmon").grid(row=0,column=0,sticky="w",padx=5)
        Label(self.frame, text=textwrap.fill(message, 20),font=("Helvetica", 9),bg="salmon").grid(row=1, column=0,sticky="w",padx=5,pady=3)
        root.update_idletasks()
        self.master.create_polygon(self.draw_triangle(self.i), fill="salmon", outline="salmon")

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2


def initial_messages(i):
    if bubbles:
        canvas.move(ALL, 0, -90)
    if i == 2:
        canvas.move(ALL, 0, -25)
    a = BotBubble(canvas, message=messages[i])
    bubbles.append(a)


def instructions():
    for i in range (1,3):
        initial_messages(i)


def clear_canvas():
    canvas.delete("all")


a = BotBubble(canvas, message=messages[0])
bubbles.append(a)
Button(root,text="CONTINUE",command=instructions).grid(row=1, column=1)
Button(root,text="NEXT SCREEN",command=clear_canvas).grid(row=1, column=2)
root.mainloop()