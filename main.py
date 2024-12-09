from Window import *
from Point import *
from Cell import *
from maze import *

def __main__():
    win = Window(1000, 1000)
    maze = Maze(50,50,16,16,50,50,win)
    maze.solve()
    win.wait_for_close()

__main__()