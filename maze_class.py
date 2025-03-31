import random
import time
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
        win = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
    
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                x1 = self._x1 + (i * self._cell_size_x)
                y1 = self._y1 + (j * self._cell_size_y)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
            
                cell = Cell(x1, y1, x2, y2, self._win)
                column.append(cell)
            
            self._cells.append(column)
            
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x_pos = self._x1 + (i * self._cell_size_x)
        y_pos = self._y1 + (j * self._cell_size_y)
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):

        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell = self._cells[self._num_cols-1][self._num_rows-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        # Mark the current cell as visited
        self._cells[i][j].visited = True

        while True:
            # List for tracking unvisited neighboring cells
            next_index_list = []

            # Check all possible neighbors and add their indices if unvisited
            # Left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # Right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # Up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # Down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # If there are no unvisited neighbors, stop and return
            if len(next_index_list) == 0:
                self._draw_cell(i, j) 
                return

            # Randomly pick one of the unvisited neighbors
            next_i, next_j = random.choice(next_index_list)

            if next_i == i - 1:  # Cell to the left
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False

            elif next_i == i + 1:  # Cell to the right
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False

            elif next_j == j - 1:  # Cell above
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            
            elif next_j == j + 1:  # Cell below
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False

            self._draw_cell(i, j)
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
    
        for row in self._cells: 
            for cell in row:
                cell.visited = False