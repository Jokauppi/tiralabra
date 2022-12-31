import pytest
import numpy as np
from game.board import Board
from ai.expectimax_ai import ExpectimaxAI
from game.board_utils import Direction, BoardState


class TestExpectimaxZigzagHeuristics:

    @pytest.fixture(autouse=True)
    def algorithm(self):
        self.algorithm = ExpectimaxAI()
        self.algorithm.set_depth(4)
        self.algorithm.set_heuristics(self.algorithm.zigzag)

    def test_instant_win(self):
        board = Board(123, initial=np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1024, 1024]]), score=10000)
        move = self.algorithm.get_move(board)
        assert move == Direction.RIGHT
        board.move(move)
        assert board.state == BoardState.WON

    def test_stick_to_right(self):
        board = Board(123, initial=np.array(
            [[0, 0, 0, 2], [0, 0, 0, 64], [0, 0, 0, 32], [0, 2, 4, 128]]), score=400)
        move = self.algorithm.get_move(board)
        assert move == Direction.UP

    def test_que_collapse(self):
        board = Board(123, initial=np.array(
            [[0, 0, 16, 32], [0, 0, 8, 64], [0, 0, 4, 128], [2, 0, 2, 256]]), score=800)

        move = self.algorithm.get_move(board)
        assert move == Direction.RIGHT
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.UP
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.UP
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.UP
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.RIGHT
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.DOWN
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.DOWN
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.DOWN
        board.move(move)

        assert 512 in board.board

    def test_reduce_to_increase(self):
        board = Board(123, initial=np.array([[0, 0, 128, 16], [0, 0, 0, 256], [
                      0, 0, 0, 128], [2, 0, 2, 1024]]), score=10000)

        move = self.algorithm.get_move(board)
        assert move == Direction.DOWN
        board.move(move)

        move = self.algorithm.get_move(board)
        assert move == Direction.RIGHT
        board.move(move)

        assert board.board[2][3] == 256

    def test_max_in_corner(self):
        board = Board(123)

        for _ in range(25):
            board.move(self.algorithm.get_move(board))

        assert board.board[3][3] == board.get_max_number()


class TestExpectimaxScoreHeuristics:

    @pytest.fixture(autouse=True)
    def algorithm(self):
        self.algorithm = ExpectimaxAI()
        self.algorithm.set_depth(4)
        self.algorithm.set_heuristics(self.algorithm.score)

    def test_instant_win(self):
        board = Board(123, initial=np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1024, 1024]]), score=18000)
        board.move(self.algorithm.get_move(board))
        board.move(self.algorithm.get_move(board))
        assert board.state == BoardState.WON

    def test_basic_move(self):
        board = Board(123, initial=np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 2]]), score=0)
        board.move(self.algorithm.get_move(board))
        board.move(self.algorithm.get_move(board))
        assert 4 in board.board

class TestExpectimaxCornerHeuristics:

    @pytest.fixture(autouse=True)
    def algorithm(self):
        self.algorithm = ExpectimaxAI()
        self.algorithm.set_depth(4)
        self.algorithm.set_heuristics(self.algorithm.corner)

    def test_instant_win(self):
        board = Board(123, initial=np.array(
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1024, 1024]]), score=18000)
        board.move(self.algorithm.get_move(board))
        assert board.state == BoardState.WON

    def test_basic_move(self):
        board = Board(123, initial=np.array(
            [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]]), score=0)
        board.move(self.algorithm.get_move(board))
        board.move(self.algorithm.get_move(board))
        assert board.board[3][3] == 4