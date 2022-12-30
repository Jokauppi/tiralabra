import numpy as np
from src.game.board import Board
from src.game.board_utils import Direction, BoardState

class TestBoardMoves:

    # Test tile movement

    def test_move_up_one_tile(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,0],[0,0,0,0],[0,0,0,0]]), score=4)
        board.move(Direction.UP)
        desired = np.array([[2,0,4,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.state == BoardState.INPROGRESS
        assert board.score == 4
        assert board.last_move == Direction.UP

    def test_move_down_one_tile(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,0],[0,0,0,0],[0,0,0,0]]), score=4)
        board.move(Direction.DOWN)
        desired = np.array([[2,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,4,0]])
        assert np.array_equal(desired, board.board)
        assert board.state == BoardState.INPROGRESS
        assert board.score == 4
        assert board.last_move == Direction.DOWN

    def test_move_left_one_tile(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,0],[0,0,0,0],[0,0,0,0]]), score=4)
        board.move(Direction.LEFT)
        desired = np.array([[2,0,0,0],[4,0,0,0],[0,0,0,0],[0,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.state == BoardState.INPROGRESS
        assert board.score == 4
        assert board.last_move == Direction.LEFT

    def test_move_right_one_tile(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,0],[0,0,0,0],[0,0,0,0]]), score=4)
        board.move(Direction.RIGHT)
        desired = np.array([[2,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.state == BoardState.INPROGRESS
        assert board.score == 4
        assert board.last_move == Direction.RIGHT