import random
from game.board_utils import Direction

class RandomAI ():
    def __init__(self):
        self.moves = [move.value for move in Direction]
    
    def get_move(self, board):
        return self.moves[random.randrange(len[self.moves])]