import numpy as np
from game.board_utils import Utils as utils
from game.board_utils import BoardState

class Board():
    def __init__(self, seed, board_size):
        self.seed = seed
        self.size = board_size
        self.board = np.ndarray((self.size,), dtype=int)
        self.state = BoardState.INPROGRESS

    def board(self):
        return self.board

    def state(self):
        return self.state

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def __update_state(self):
        pass

    def __add_number(self):
        pass

    def __get_row(self):
        pass

    def __get_column(self):
        pass