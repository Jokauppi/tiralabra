import numpy as np
from game.board_utils import Utils as utils
from game.board_utils import BoardState
import random

class Board():
    def __init__(self, seed, board_size, initial = None):
        self.seed = seed
        random.seed(self.seed)
        self.size = board_size
        if initial == None:
            self.board = np.zeros((self.size, self.size), dtype=int)
            self.__add_number()
            self.__add_number()
        else:
            self.board = initial
        self.state = BoardState.INPROGRESS

    def up(self):
        print("↑")
        modified=False
        for col in range(self.size):
            old_line = self.__get_column(col)
            (new_line, line_modified) = utils.move_line_backwards(old_line)
            if line_modified:
                self.__set_column(col, new_line)
                modified = True
        if modified:
            self.__add_number()

    def down(self):
        print("↓")
        modified=False
        for col in range(self.size):
            old_line = self.__get_column(col)
            (new_line, line_modified) = utils.move_line_forwards(old_line)
            if line_modified:
                self.__set_column(col, new_line)
                modified = True
        if modified:
            self.__add_number()

    def left(self):
        print("←")
        modified=False
        for row in range(self.size):
            old_line = self.__get_row(row)
            (new_line, line_modified) = utils.move_line_backwards(old_line)
            if line_modified:
                self.__set_row(row, new_line)
                modified = True
        if modified:
            self.__add_number()

    def right(self):
        print("→")
        modified=False
        for row in range(self.size):
            old_line = self.__get_row(row)
            (new_line, line_modified) = utils.move_line_forwards(old_line)
            if line_modified:
                self.__set_row(row, new_line)
                modified = True
        if modified:
            self.__add_number()

    def __check_state(self):
        pass

    # Add a 2 or 4 on an empty tile, with 4 having a 10% chance of appearing istead of a 2
    def __add_number(self):
        empty_tiles = utils.empty_tiles(self)
        chosen_tile = empty_tiles[random.randrange(len(empty_tiles))]
        new_number = 2
        if random.randrange(10) == 0:
            new_number = 4
        self.board[chosen_tile[0]][chosen_tile[1]] = new_number

    def __get_row(self, index):
        return self.board[index, :]

    def __get_column(self, index):
        return self.board[:, index]

    def __set_row(self, index, values):
        self.board[index, :] = values

    def __set_column(self, index, values):
        self.board[:, index] = values