from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.title = ""
        self.canvas = Canvas()
        self.canvas.pack()
        self.window_is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()
    
    def close(self):
        self.window_is_running = False
