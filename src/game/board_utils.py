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
        
        p1=len(line)-2
        p2=len(line)-1
        while True:
            if p1==-1:
                break
            elif line[p1]>0 and line[p2]==0:
                line[p2]=line[p1]
                line[p1]=0
                p1-=1
            elif line[p1]==0:
                p1-=1
            elif line[p1]==line[p2]:
                line[p2]=line[p1]+line[p2]
                line[p1]=0
                p1-=1
                p2-=1
            elif line[p1]>0 and line[p2]>0:
                if p2-1==p1:
                    p1-=1
                    p2-=1
                else:
                    p2-=1
            else:
                raise Exception("unnoticed line push case")
        
        return line

    def move_line_backwards(line):

        return line

class BoardState(Enum):
    INPROGRESS = 1
    LOST = 2
    WON = 3
