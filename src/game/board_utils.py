import numpy as np
from enum import Enum

class Utils():
    def __init__(self):
        pass
    
    def empty_tiles(board):
        tiles = board.board
        empty_tiles = []
        with np.nditer(tiles, flags=['multi_index'], op_flags=['readwrite']) as it:
            for tile in it:
                if tile == 0:
                    empty_tiles.append(it.multi_index)
        return(empty_tiles)

    def move_line_forwards(line):
        pass

    def move_line_backwards(line):
        pass

class BoardState(Enum):
    INPROGRESS = 1
    LOST = 2
    WON = 3
