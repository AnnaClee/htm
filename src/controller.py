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
        new_frame = frame_class(self.window, self)

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = new_frame
        self.current_frame.tkraise()