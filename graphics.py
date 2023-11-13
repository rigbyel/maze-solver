from textwrap import fill
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isRunning = True
        while(self.__isRunning):
            self.redraw()

    def close(self):
        self.__isRunning = False
        print("The window is closed")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.__p1 = point1
        self.__p2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.__p1.x, self.__p1.y,
                        self.__p2.x, self.__p2.y,
                        fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)


    