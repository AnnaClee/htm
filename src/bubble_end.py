from tkinter import *
from datetime import datetime
import textwrap

from src.base_gui import BaseGUI
from src.bubble_start import BotBubble


class ChatScreen(BaseGUI):
    def __init__(self, master, controller):
        super(ChatScreen,self).__init__(master,controller)
        self.canvas = Canvas(self, width=500, height=500, bg="white")
        self.canvas.grid(row=0)
        self.bubbles = []
        Button(self, text="CONTINUE", command=self.instructions).grid(row=1, column=0)

    # This probably needs updating
    def instructions(self):
        messages = ["CONGRATULATIONS! You lured your target into revealing their password and information by clicking on a phishing link.",
                    "Wasn't that scarily easy?! I hope you realise how careful you yourself need to be!",
                    "Only open a link if it's from a trusted source (somebody you know) and you are expecting to recieve it."
                    "Getting hacked is not cool!"]
        for i, msg in enumerate(messages):
            self.canvas.move(ALL, 0, -110)
            a = BotBubble(self.master,self.controller, self.canvas, msg)
            self.bubbles.append(a)
