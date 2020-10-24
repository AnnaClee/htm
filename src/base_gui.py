from tkinter import *
import tkinter as tk

class BaseGUI(tk.Frame):
    def __init__(self, master, controller, title="", bg=""):
        super(BaseGUI, self).__init__(master, bg=bg)
        self.controller = controller
        self.master = master
        master.title(title)# title of the window
        self.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    # Test the class here

    # This should create an empty window with title Hello
    window1 = Tk()
    BaseGUI(window1, "Hello")
    window1.mainloop()
