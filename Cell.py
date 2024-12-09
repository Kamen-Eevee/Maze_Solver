from Point import *

class Cell():
    def __init__(self, window=None):
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self.win = window
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False

    def draw(self, point1, point2):
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        line_top = Line(point1, Point(point2.x, point1.y))
        line_bottom = Line(Point(point1.x, point2.y), point2)
        line_left = Line(point1, Point(point1.x, point2.y))
        line_right = Line(Point(point2.x, point1.y), point2)
        if self.win != None:
            if self.left_wall:
                self.win.draw_line(line_left)
            else:
                self.win.draw_line(line_left, "#d9d9d9")
            if self.right_wall:
                self.win.draw_line(line_right)
            else:
                self.win.draw_line(line_right, "#d9d9d9")
            if self.top_wall:
                self.win.draw_line(line_top)
            else:
                self.win.draw_line(line_top, "#d9d9d9")
            if self.bottom_wall:
                self.win.draw_line(line_bottom)
            else:
                self.win.draw_line(line_bottom, "#d9d9d9")

    def draw_move(self, to_cell, undo = False):
        center_point_1 = self._get_center()
        center_point_2 = to_cell._get_center()
        line = Line(center_point_1, center_point_2)
        if undo == False:
            line.draw(self.win.canvas, "red")
        else:
            line.draw(self.win.canvas, "gray")

    def _get_center(self):
        return Point(self._x1 + (self._x2 - self._x1)//2, self._y1 + (self._y2-self._y1)//2)