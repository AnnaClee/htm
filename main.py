from src.helloworld_gui import HelloWorld
from tkinter import *
from src.controller import Controller


if __name__ == "__main__":

    # I've used HelloWorld as an example here, replace this with your own object / code
    window1 = Tk()
    c = Controller(window1, HelloWorld)
    c.start()

