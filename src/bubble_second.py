from tkinter import *
from datetime import datetime
import textwrap

from src.base_gui import BaseGUI
from src.bubble_start import BotBubble


class ChatScreen2(BaseGUI):
    def __init__(self, master, controller):
        super(ChatScreen2,self).__init__(master,controller)
        self.canvas = Canvas(self, width=500, height=500, bg="white")
        self.canvas.grid(row=0)
        self.bubbles = []
        Button(self, text="SHOW INSTRUCTIONS", command=self.instructions).grid(row=1, column=0)
        Button(self, text="NEXT SCREEN", command=self.next_screen).grid(row=1, column=1)

    # This probably needs updating
    def instructions(self):
        messages = ["We're in! Now we move on to the next phase of our hacking operation!",
                    "Wouldn't it be funny if we could access this person's facebook account to make a silly post.",
                    "On the next screen you will see the desktop: Click to open facebook and then attempt to login using the same credentials as before.",
                    "If we can't get in we will have to try and trick the person into giving us our data! With a phishing attack to their emails."]
        for i, msg in enumerate(messages):
            self.canvas.move(ALL, 0, -110)
            a = BotBubble(self.master,self.controller, self.canvas, msg)
            self.bubbles.append(a)

    def next_screen(self):
        self.controller.switch_frame("image")
