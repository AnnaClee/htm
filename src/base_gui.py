from tkinter import *


class BaseGUI:
    def __init__(self, master, title=""):
        self.master = master
        master.title(title)# title of the window
        master.geometry("1024x576")


if __name__ == "__main__":
    # Test the class here

    # This should create an empty window with title Hello
    window1 = Tk()
    BaseGUI(window1, "Hello")
    window1.mainloop()
