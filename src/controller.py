from src.login import PasswordGUI
from src.bubble_start import ChatScreen
from src.bubble_second import ChatScreen2
from src.bubble_end import ChatScreen3
from src.Tkinter_image import TkinterImage
from src.helloworld_gui import HelloWorld, SecondFrame
from src.login2 import PasswordGUI2

classes = {"login":PasswordGUI, "chat":ChatScreen, "image":TkinterImage, "hello": HelloWorld, "second":SecondFrame,
           "login2":PasswordGUI2, "chat2":ChatScreen2, "chat3":ChatScreen3}

class Controller:
    def __init__(self, window, start_frame):
        self.window = window
        self.current_frame = None
        self.switch_frame(start_frame)
        self.window.geometry("1024x576")

    def start(self):
        self.window.mainloop()

    def switch_frame(self, frame_class):
        print("I is called")
        new_frame = classes[frame_class](self.window, self)

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = new_frame
        self.current_frame.tkraise()