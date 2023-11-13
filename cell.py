import re
from graphics import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self._win == None:
            return
        
        # drawing left wall
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line, "black" if self.has_left_wall else "white")
        
        # drawing top wall
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(line, "black" if self.has_top_wall else "white")
        
        # drawing right wall
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(line, "black" if self.has_right_wall else "white")
        
        # drawing bottom wall
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        if self._win == None:
            return
        start = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        end = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        
        line_color = "gray" if undo else "red"

        if start.x != end.x:
            self._win.draw_line(Line(start, Point(end.x, start.y)), line_color)
        if start.y != end.y:
            self._win.draw_line(Line(Point(end.x, start.y), end), line_color)
        
    def break_wall(self, wall):
        match wall:
            case "top":
                self.has_top_wall = False
            case "bottom":
                self.has_bottom_wall = False
            case "right":
                self.has_right_wall = False
            case "left":
                self.has_left_wall = False
        self.draw()