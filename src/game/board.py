from typing import Optional
import numpy as np
from game.board_utils import Utils as utils
from game.board_utils import BoardState, Direction
import random


class Board():
    def __init__(self, seed: int, board_size: int, initial = None):
        self.seed = seed
        random.seed(self.seed)
        self.size = board_size
        if initial is None:
            self.board = np.zeros((self.size, self.size), dtype=int)
            self.__add_number()
            self.__add_number()
        else:
            self.board = initial
        self.state = BoardState.INPROGRESS

    def move(self, direction: Direction, add_number=True, check_state=True):
        modified = False

        for line in range(self.size):

            if direction == Direction.UP or direction == Direction.DOWN:

                old_line = self.__get_column(line)

                if direction == Direction.UP:
                    (new_line, line_modified) = utils.move_line_backwards(old_line)
                else:
                    (new_line, line_modified) = utils.move_line_forwards(old_line)

                if line_modified:
                    self.__set_column(line, new_line)
                    modified = True

            else:
                old_line = self.__get_row(line)

                if direction == Direction.LEFT:
                    (new_line, line_modified) = utils.move_line_backwards(old_line)
                else:
                    (new_line, line_modified) = utils.move_line_forwards(old_line)
                
                if line_modified:
                    self.__set_row(line, new_line)
                    modified = True

        if modified and add_number:
            self.__add_number()

        if check_state:
            self.check_state()

    def check_state(self):
        if self.check_win():
            self.state = BoardState.WON
        elif self.check_loss():
            self.state = BoardState.LOST

    def check_win(self):
        if 2048 in self.board.flatten(): return True

    def check_loss(self):
        for row in range(self.size):
            line = self.__get_row(row)
            if utils.is_line_movable(line): return False
        for col in range(self.size):
            line = self.__get_column(col)
            if utils.is_line_movable(line): return False
        return True

    # Add a 2 or 4 on an empty tile, with 4 having a 10% chance of appearing
    # istead of a 2
    def __add_number(self):
        empty_tiles = self.empty_tiles()
        chosen_tile = empty_tiles[random.randrange(len(empty_tiles))]
        new_number = 2
        if random.randrange(10) == 0:
            new_number = 4
        self.board[chosen_tile[0]][chosen_tile[1]] = new_number

    def empty_tiles(self):
        empty_tiles = []
        with np.nditer(self.board, flags=['multi_index'], op_flags=['readwrite']) as it:
            for tile in it:
                if tile == 0:
                    empty_tiles.append(it.multi_index)
        return (empty_tiles)

    def __get_row(self, index):
        return self.board[index, :]

    def __get_column(self, index):
        return self.board[:, index]

    def __set_row(self, index, values):
        self.board[index, :] = values

    def __set_column(self, index, values):
        self.board[:, index] = values

    def __str__(self) -> str:
        utils.print_board(self.board, self.size)

    def __copy__(self):
        return Board(self.seed, self.board_size, initial=self.board.copy())