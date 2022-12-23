from typing import Optional
import numpy as np
from game.board_utils import Utils as utils
from game.board_utils import BoardState, Direction
import random


class Board():
    def __init__(self, seed: int, board_size: int = 4, initial=None, score=0, set_seed=True):
        self.seed = seed
        if set_seed:
            random.seed(self.seed)
        self.size = board_size
        if initial is None:
            self.board = np.zeros((self.size, self.size), dtype=int)
            self.__add_number()
            self.__add_number()
        else:
            self.board = initial
        self.state = BoardState.INPROGRESS
        self.score = score
        self.immovable_direction = None
        self.last_move = None

    def move(self, direction: Direction, add_number=True, check_state=True):

        modified = False
        move_score = 0

        for line in range(self.size):

            if direction == Direction.UP or direction == Direction.DOWN:

                old_line = self.__get_column(line)

                if direction == Direction.UP:
                    (new_line, line_modified,
                     line_score) = utils.move_line_backwards(old_line)
                else:
                    (new_line, line_modified,
                     line_score) = utils.move_line_forwards(old_line)

                if line_modified:
                    self.__set_column(line, new_line)
                    modified = True

                move_score += line_score

            else:
                old_line = self.__get_row(line)

                if direction == Direction.LEFT:
                    (new_line, line_modified,
                     line_score) = utils.move_line_backwards(old_line)
                else:
                    (new_line, line_modified,
                     line_score) = utils.move_line_forwards(old_line)

                if line_modified:
                    self.__set_row(line, new_line)
                    modified = True

                move_score += line_score

        if modified:
            if add_number:
                self.__add_number()

            self.immovable_direction = None
        else:
            self.immovable_direction = direction

        if check_state:
            self.check_state()

        self.last_move = direction
        self.score += move_score

    def check_state(self):
        if self.check_win():
            self.state = BoardState.WON
        elif self.check_loss():
            self.state = BoardState.LOST

    def check_win(self):
        if 2048 in self.board.flatten():
            return True

    def check_loss(self):
        for row in range(self.size):
            line = self.__get_row(row)
            if utils.is_line_movable(line):
                return False
        for col in range(self.size):
            line = self.__get_column(col)
            if utils.is_line_movable(line):
                return False
        return True

    def put_number(self, tile, number):
        self.board[tile[0]][tile[1]] = number

    def empty_tiles(self):
        empty_tiles = []
        with np.nditer(self.board, flags=['multi_index'], op_flags=['readwrite']) as it:
            for tile in it:
                if tile == 0:
                    empty_tiles.append(it.multi_index)
        return (empty_tiles)

    def possible_new_numbers(self):
        empty_tiles = self.empty_tiles()
        moves = []
        for tile in empty_tiles:
            moves.append((tile, 2, 0.9))
            moves.append((tile, 4, 0.1))
        return moves

    def get_size(self):
        return self.size
    # Add a 2 or 4 on an empty tile, with 4 having a 10% chance of appearing
    # istead of a 2

    def __add_number(self):
        empty_tiles = self.empty_tiles()
        chosen_tile = empty_tiles[random.randrange(len(empty_tiles))]
        new_number = 2
        if random.randrange(10) == 0:
            new_number = 4
        self.board[chosen_tile[0]][chosen_tile[1]] = new_number

    def get_max_number(self):
        return max(self.board.flatten())

    def __get_row(self, index):
        return self.board[index, :]

    def __get_column(self, index):
        return self.board[:, index]

    def __set_row(self, index, values):
        self.board[index, :] = values

    def __set_column(self, index, values):
        self.board[:, index] = values

    def __str__(self) -> str:
        utils.print_board(self)

    def __copy__(self):
       new_board = Board(self.seed, self.size, initial=self.board.copy(), score=self.score, set_seed=False)
       new_board.last_move = self.last_move
       new_board.immovable_direction = self.immovable_direction
       return new_board
