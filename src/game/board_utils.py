import numpy as np
from enum import Enum

class Utils():
    def __init__(self, seed):
        self.seed = seed
    
    def select_random_empty_tile(board):
        pass

    def move_line_forwards():
        pass

    def move_line_backwards():
        pass

class BoardState(Enum):
    INPROGRESS = 1
    LOST = 2
    WON = 3
