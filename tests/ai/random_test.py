import pytest
import numpy as np
from game.board import Board
from ai.random_ai import RandomAI
from game.board_utils import Direction, BoardState


class TestRandomMoves:

    @pytest.fixture(autouse=True)
    def algorithm(self):
        self.algorithm = RandomAI()

    def test_random(self):
        board = Board(123)
        moves = []
        for _ in range(200):
            move = self.algorithm.get_move(board)
            assert move in [
                Direction.RIGHT,
                Direction.LEFT,
                Direction.UP,
                Direction.DOWN]
            moves.append(move)
        assert Direction.UP in moves and Direction.RIGHT in moves
