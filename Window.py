from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, height = height, width = width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.run = False
        self.root.protocol("WM_DELETE_WINDOW", self.close())

    def draw_line(self, line, color="black"):
        line.draw(self.canvas, color)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.run = True
        while self.run == True:
            self.redraw()

    def close(self):
        self.run = False