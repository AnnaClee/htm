from src.helloworld_gui import HelloWorld
from tkinter import *
from src.controller import Controller
from src.Tkinter_image import TkinterImage


if __name__ == "__main__":

    # # I've used HelloWorld as an example here, replace this with your own object / code
    # window1 = Tk()
    # HelloWorld(window1)
    # window1.mainloop()
    window = Tk()
    app = Controller(window, "chat")
    app.start()
    window.mainloop()

