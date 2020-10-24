from tkinter import *
from datetime import datetime
import textwrap

from src.base_gui import BaseGUI
from src.controller import Controller
from src.helloworld_gui import HelloWorld


# Before

# class BotBubble():
#     def __init__(self,master,message=""):
#         self.master = master
#         self.frame = Frame(master,bg="salmon")
#         self.i = self.master.create_window(90,400,window=self.frame)
#         Label(self.frame,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="salmon").grid(row=0,column=0,sticky="w",padx=5)
#         Label(self.frame, text=textwrap.fill(message, 20),font=("Helvetica", 9),bg="salmon").grid(row=1, column=0,sticky="w",padx=5,pady=3)
#         root.update_idletasks()
#         self.master.create_polygon(self.draw_triangle(self.i), fill="salmon", outline="salmon")
#
#     def draw_triangle(self,widget):
#         x1, y1, x2, y2 = self.master.bbox(widget)
#         return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2
#
# def initial_messages(i):
#     if bubbles:
#         canvas.move(ALL, 0, -90)
#     if i == 2:
#         canvas.move(ALL, 0, -25)
#     a = BotBubble(canvas, message=messages[i])
#     bubbles.append(a)
#
#
# def instructions():
#     for i in range (1,3):
#         initial_messages(i)
#
#
# def clear_canvas():
#     canvas.delete("all")
#
#
#
# if __name__ == "__main__":
#     root = Tk()
#     root.config(bg="white")
#
#     canvas = Canvas(root, width=1024, height=576, bg="white")
#     canvas.grid(row=0, column=0, columnspan=3)
#
#     bubbles = []
#     messages = ["Hello and welcome to our internet safety game! Click CONTINUE to proceed.",
#                 "I am here to explain how things will work.",
#                 "Firstly we ask you to login by typing a password to enter with the username shown. Click NEXT SCREEN to advance screens."]
#     a = BotBubble(canvas, message=messages[0])
#     bubbles.append(a)
#     Button(root,text="CONTINUE",command=instructions).grid(row=1, column=1)
#     Button(root,text="NEXT SCREEN",command=clear_canvas).grid(row=1, column=2)
#     root.mainloop()


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
        self.controller.switch_frame(HelloWorld)



if __name__ == "__main__":
    window = Tk()
    c = Controller(window,ChatScreen)
    c.start()