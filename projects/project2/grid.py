from datastructures.array2d import Array2D
from projects.project2.cell import Cell
import random

class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height 

        cells = []

        for row in range(height):
            cells.append([])

            for col in range(width):
                is_alive = random.choice([True, False])
                cells[row].append(Cell(is_alive = is_alive))

        self.grid: Array2D[Cell] = Array2D(starting_sequence = cells, data_type = Cell)

    def __str__(self):
        grid = ""
        for row in range(self.height):
            for col in range(self.width):
                grid += str(self.grid[row][col])
            grid += "\n"
        return grid

    def __eq__(self, previous):
        if not isinstance(previous, Grid):
            return False
        
        return self.grid == previous.grid

    def check_neigh(self,row_index, col_index):
        counter = 0
        for row in range(row_index - 1, row_index + 2):
            for col in range(col_index - 1, col_index + 2):
                if (row_index == row and col_index == col) or not (0 <= row < self.height and 0<= col < self.width):
                    continue
                
                if self.grid[row][col].is_alive():
                    counter += 1
        return counter
    

    def new_gen(self):

        new_grid = Grid(self.width,self.height)
        for row in range(self.height):
            for col in range(self.width):
                if self.check_neigh(row, col) == 3:
                    new_grid.grid[row][col].set_alive(True)
                
                elif self.check_neigh(row, col) == 2: 
                    new_grid.grid[row][col].set_alive(self.grid[row][col].is_alive())

                else:
                    new_grid.grid[row][col].set_alive(False)
        
        return new_grid
                



    def display(self):
        print(self)
        #print(self.check_neigh(0,0))