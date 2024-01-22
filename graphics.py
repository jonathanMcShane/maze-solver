from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.__root = Tk()
        self.__root.title = ""
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__window_is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_is_running = True
        while self.__window_is_running:
            self.redraw()
    
    def close(self):
        self.__window_is_running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)

class Line:

    def __init__(self, point_a, point_b):
        self.__point_a = point_a
        self.__point_b = point_b

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.__point_a.x, self.__point_a.y, self.__point_b.x, self.__point_b.y, fill=fill_colour, width=2
        )
        canvas.pack()
    
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y