from operator import ne
import time
import random
from cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
            ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y =cell_size_y
        self._cells = []
        self.__win = win
        
        if seed != None:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        print("The maze is ready to solve")

    def _create_cells(self):
        for i in range(self.__num_rows):
            self._cells.append([])
            for j in range(self.__num_cols):
                self._cells[i].append( Cell( 
                                          self.__x1 + i*self.__cell_size_x,
                                          self.__y1 + j*self.__cell_size_y,
                                          self.__x1 + (i + 1)*self.__cell_size_x,
                                          self.__y1 + (j + 1)*self.__cell_size_y,
                                          self.__win
                                          )
                                        )   
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.__win == None:
            return 
        self.__win.redraw()
        time.sleep(0.035)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.__num_rows - 1, self.__num_cols - 1)

    def _break_walls_r(self, i, j):
        while(True):
            current_cell = self._cells[i][j]
            current_cell.visited = True
            dirs = []

            if i > 0 and not self._cells[i-1][j].visited:
                dirs.append((i-1,j))
            if j > 0 and not self._cells[i][j-1].visited:
                dirs.append((i,j-1))
            if i < self.__num_rows - 1 and not self._cells[i+1][j].visited:
                dirs.append((i+1, j))
            if j < self.__num_cols - 1 and not self._cells[i][j+1].visited:
                dirs.append((i, j+1))

            if len(dirs) == 0:
                break

            next = random.choice(dirs)
            next_cell = self._cells[next[0]][next[1]]
            dirs.remove(next)
            if next[0] < i:
                next_cell.break_wall("right")
                current_cell.break_wall("left")
            if next[0] > i:
                next_cell.break_wall("left")
                current_cell.break_wall("right")
            if next[1] < j:
                next_cell.break_wall("bottom")
                current_cell.break_wall("top")
            if next[1] > j:
                next_cell.break_wall("top")
                current_cell.break_wall("bottom")
            self._animate()
            
            self._break_walls_r(next[0], next[1])
        return
    
    def _reset_cells_visited(self):
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self._cells[i][j].visited = False
    
    def solve_r(self, i, j):
        if i == self.__num_rows - 1 and j == self.__num_cols - 1:
            return True
        solved = False
        current_cell = self._cells[i][j]
        current_cell.visited = True

        dirs = []
        if i > 0 and not current_cell.has_left_wall and not self._cells[i-1][j].visited:
            dirs.append((i-1,j))
        if j > 0 and not current_cell.has_top_wall and not self._cells[i][j-1].visited:
            dirs.append((i,j-1))
        if i < self.__num_rows - 1 and not current_cell.has_right_wall and not self._cells[i+1][j].visited:
            dirs.append((i+1,j))
        if i < self.__num_cols - 1 and not current_cell.has_bottom_wall and not self._cells[i][j+1].visited:
            dirs.append((i,j+1))

        if len(dirs) == 0:
            return False
        
        for next in dirs:
            next_cell = self._cells[next[0]][next[1]]
            current_cell.draw_move(next_cell)
            self._animate()
            solved = self.solve_r(next[0], next[1])
            if solved:
                return True
            current_cell.draw_move(next_cell, undo=True)
            self._animate()

