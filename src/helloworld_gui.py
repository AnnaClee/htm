from src.base_gui import BaseGUI
from tkinter import *


class HelloWorld(BaseGUI):
    def __init__(self, master_window):
        #  calling parent constructor:
        super(HelloWorld, self).__init__(master_window, "Hello World")
        self.label = Label(master_window, text="Hello There!")
        # It is important that .grid() is done on a different line as otherwise self.label = None
        self.label.grid(row=0, column=0)

        self.clickbutton = Button(master_window, text="CLICK ME", command=self.on_button_click)
        self.clickbutton.grid(row=1, column=0)

    def on_button_click(self):
        self.update_label("Hey, you clicked the button :)")

    def update_label(self, new_text):
        self.label['text'] = new_text


if __name__ == "__main__":
    # Any testing specific to this class should be done here
    window1 = Tk()
    HelloWorld(window1)
    window1.mainloop()