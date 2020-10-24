from tkinter import *
from datetime import datetime
import textwrap

from src.base_gui import BaseGUI

class BotBubble(BaseGUI):
    def __init__(self,master,controller,canvas,message):
        super(BotBubble,self).__init__(master,controller, bg="salmon")
        # self.i = self.create_window(90,400,window=self)
        canvas.create_window(90,400, window=self)
        self.time = Label(self,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="salmon")
        self.msg = Label(self, text=textwrap.fill(message, 20),font=("Helvetica", 9),bg="salmon")
        self.time.grid(row=0,column=0,sticky="w",padx=5)
        self.msg.grid(row=1, column=0,sticky="w",padx=5,pady=3)

class ChatScreen(BaseGUI):
    def __init__(self, master, controller):
        super(ChatScreen,self).__init__(master,controller)
        self.canvas = Canvas(self, width=500, height=500, bg="white")
        self.canvas.grid(row=0)
        self.bubbles = []
        Button(self, text="CONTINUE", command=self.instructions).grid(row=1, column=0)
        Button(self, text="NEXT SCREEN", command=self.next_screen).grid(row=1, column=1)

    # This probably needs updating
    def instructions(self):
        messages = ["Hello and welcome to our internet safety game! Click CONTINUE to proceed.",
                    "I am here to explain how things will work.",
                    "Firstly we ask you to login by typing a password to enter with the username shown. Click NEXT SCREEN to advance screens."]
        for i, msg in enumerate(messages):
            self.canvas.move(ALL, 0, -150)
            a = BotBubble(self.master,self.controller, self.canvas, msg)
            self.bubbles.append(a)

    def next_screen(self):
        self.controller.switch_frame("login")

