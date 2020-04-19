#!/usr/bin/env python2

import random

class Cell(object):

    def __init__(self, has_mine):
        self.__has_mine = has_mine
        self.__revealed = False

    def has_mine(self):
        return self.__has_mine

    def reveal(self):
        self.__revealed = True

    def is_revealed(self):
        return self.__revealed

    def render(self):
        if revealed:
            return 'X' if has_mine else '_'
        else:
            return '-'

class Grid(object):

    def __init__(self, height, width, num_mines):
        self.__height = height
        self.__width = width
        self.__num_mines = num_mines
        self.__initgrid(0)
    
    def __initgrid(self):
        num_cells = self.__height * self.__width
        prob = float(self.__num_mines) / num_cells

        self.__grid = [[None]*width for i in range(height)]

        for row in range(self.__height):
            for col in range(self.__width):
                has_mine = False
                if random.random() < prob:
                    has_mine = True
                self.__grid[row][col] = Cell(has_mine)

    def reveal_cell(self, row, col):
        if row < 0 or col < 0 or row >= self.__height or col >= self.__width:
            return
        self.__grid[i][j].reveal()
        if self.__grid[row][col].has_mine():
            return False
        else:
            for i in [row-1, row, row+1]:
                for j in [col-1, col, row+1]:

    def render(self):
        pass
