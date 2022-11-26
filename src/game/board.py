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
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def __check_state(self):
        pass

    def __add_number(self):
        empty_tiles = utils.empty_tiles(self)
        chosen_tile = empty_tiles[random.randrange(len(empty_tiles))]
        print(chosen_tile)
        self.board[chosen_tile[0]][chosen_tile[1]] = 2      

    def __get_row(self):
        pass

    def __get_column(self):
        pass