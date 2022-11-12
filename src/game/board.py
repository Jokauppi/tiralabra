import numpy as np

class Board():
    def __init__(self, seed, board_size):
        self.seed = seed
        self.size = board_size

    def view(self):
        seed = self.seed_ui.view()
        board_size = 4
        board = np.ndarray((size,), dtype=int)