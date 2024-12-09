from Cell import *
from Window import *
from random import *

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, num_seed = None):
        #start position of the entire maze (top left corner)
        self.x = x1
        self.y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if num_seed != None:
            seed(num_seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        if num_rows > 1 and num_cols > 1:
            self._break_walls_r(0,0)
            self._reset_cells_visited()

    def _create_cells(self):
        for column in range(0, self.num_cols):
            cell_list = []
            for row in range(0, self.num_rows):
                cell_list.append(Cell(self.win))
            self._cells.append(cell_list)
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        point_1 = Point(self.x+(self.cell_size_x*i), self.y+(self.cell_size_y*j))
        point_2 = Point(self.x+(self.cell_size_x*(i+1)),self.y+(self.cell_size_y*(j+1)))
        self._cells[i][j].draw(point_1,point_2)
        self._animate()
    
    def _animate(self):
        if self.win != None:
            self.win.redraw()
            self.win.root.after(50)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _reset_cells_visited(self):
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._cells[i][j].visited = False

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while 1:
            unvisited = []
            if i > 0 and i < self.num_cols - 1:
                if self._cells[i+1][j].visited == False:
                    unvisited.append(self._cells[i+1] [j])
                if self._cells[i-1][j].visited == False:
                    unvisited.append(self._cells[i-1] [j])
            elif i == 0:
                if self._cells[i+1][j].visited == False:
                    unvisited.append(self._cells[i+1] [j])
            elif i == self.num_cols-1:
                if self._cells[i-1][j].visited == False:
                    unvisited.append(self._cells[i-1] [j])
            
            if j > 0 and j < self.num_rows-1:
                if self._cells[i][j+1].visited == False:
                    unvisited.append(self._cells[i] [j+1])
                if self._cells[i][j-1].visited == False:
                    unvisited.append(self._cells[i] [j-1])
            elif j == 0:
                if self._cells[i][j+1].visited == False:
                    unvisited.append(self._cells[i] [j+1])
            elif j == self.num_rows-1:
                if self._cells[i][j-1].visited == False:
                    unvisited.append(self._cells[i] [j-1])

            if unvisited == []:
                self._draw_cell(i,j)
                return
            next_cell = unvisited[randrange(0, len(unvisited))]

            if next_cell._x1 > self._cells[i][j]._x1:
                new_i = i+1
                new_j = j
                self._cells[i][j].right_wall = False
                next_cell.left_wall = False
            if next_cell._x1 < self._cells[i][j]._x1:
                new_i = i-1
                new_j = j
                self._cells[i][j].left_wall = False
                next_cell.right_wall = False
            if next_cell._y1 > self._cells[i][j]._y1:
                new_i = i
                new_j = j+1
                self._cells[i][j].bottom_wall = False
                next_cell.top_wall = False
            if next_cell._y1 < self._cells[i][j]._y1:
                new_i = i
                new_j = j-1
                self._cells[i][j].top_wall = False
                next_cell.bottom_wall = False
            
            self._break_walls_r(new_i, new_j)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self.num_cols-1][self.num_rows-1]:
            return True
        

        if j + 1 <= self.num_rows and self._cells[i][j].bottom_wall == False:
            if self._cells[i][j+1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                way_to_exit = self._solve_r(i, j+1)
                if way_to_exit == False:
                    self._cells[i][j].draw_move(self._cells[i][j+1], True)
                else:
                    return True
        
        if i + 1 <= self.num_cols - 1 and self._cells[i][j].right_wall == False:
            if self._cells[i+1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                way_to_exit = self._solve_r(i+1, j)
                if way_to_exit == False:
                    self._cells[i][j].draw_move(self._cells[i+1][j], True)
                else:
                    return True
                
        if i - 1 >= 0 and self._cells[i][j].left_wall == False:
            if self._cells[i-1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                way_to_exit = self._solve_r(i-1, j)
                if way_to_exit == False:
                    self._cells[i][j].draw_move(self._cells[i-1][j], True)
                else:
                    return True
                
        if j - 1 >= 0 and self._cells[i][j].top_wall == False:
            if self._cells[i][j-1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                way_to_exit = self._solve_r(i, j-1)
                if way_to_exit == False:
                    self._cells[i][j].draw_move(self._cells[i][j-1], True)
                else:
                    return True
        
       
                
        return False

    def solve(self):
        return self._solve_r(i=0, j=0)