"""
Provides a game algorithm class for generating random moves.
"""

import random
from game.board_utils import Direction


class RandomAI ():
    """
    Algorithm for generating random moves.
    """

    def __init__(self):
        self.moves = [
            Direction.UP,
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT]

    def get_move(self, _):
        """
        Generate one random move.

        Parameters:
            _ (Board): Board state (unused to conform to the get_move method of other algorithms)

        Returns:
            Direction: Direction to move
        """
        return self.moves[random.randrange(len(self.moves))]
