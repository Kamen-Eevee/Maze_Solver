

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, Point1, Point2):
        self.point_1 = Point1
        self.point_2 = Point2

    def draw(self, canvas, color="black"):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill = color, width = 2)
