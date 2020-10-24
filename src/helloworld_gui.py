from src.base_gui import BaseGUI
from tkinter import *

from src.controller import Controller


class SecondFrame(BaseGUI):
    def __init__(self, master_window, controller):
        #  calling parent constructor:
        super(SecondFrame, self).__init__(master_window, controller, "Second Frame")

        self.label = Label(master_window, text="You Have Switched")
        # It is important that .grid() is done on a different line as otherwise self.label = None
        self.label.grid(row=1, column=1)



class HelloWorld(BaseGUI):
    def __init__(self, master_window, controller):
        #  calling parent constructor:
        super(HelloWorld, self).__init__(master_window, controller, "Hello World")

        self.label = Label(self, text="Hello There!")
        # It is important that .grid() is done on a different line as otherwise self.label = None
        self.label.grid(row=1, column=1)

        self.clickbutton = Button(self, text="CLICK ME", command=self.on_button_click)
        self.clickbutton.grid(row=2, column=1)

    def on_button_click(self):
        # This switches to SecondFrame
        self.controller.switch_frame(SecondFrame)

    def update_label(self, new_text):
        self.label['text'] = new_text


if __name__ == "__main__":
    # Any testing specific to this class should be done here
    window = Tk()
    app = Controller(window, HelloWorld)
    app.start()
