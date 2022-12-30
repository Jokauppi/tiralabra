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

    # Multiple tiles

    def test_move_up_multiple_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,2],[0,0,0,8],[0,128,0,0]]))
        board.move(Direction.UP)
        desired = np.array([[2,128,4,2],[0,0,0,8],[0,0,0,0],[0,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.score == 0

    def test_move_down_multiple_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,2],[0,0,0,8],[0,128,0,0]]))
        board.move(Direction.DOWN)
        desired = np.array([[2,0,0,0],[0,0,0,0],[0,0,0,2],[0,128,4,8]])
        assert np.array_equal(desired, board.board)
        assert board.score == 0

    def test_move_left_multiple_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,2],[0,0,0,8],[0,128,0,0]]))
        board.move(Direction.LEFT)
        desired = np.array([[2,0,0,0],[4,2,0,0],[8,0,0,0],[128,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.score == 0

    def test_move_right_multiple_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,4,2],[0,0,0,8],[0,128,0,0]]))
        board.move(Direction.RIGHT)
        desired = np.array([[2,0,0,0],[0,0,4,2],[0,0,0,8],[0,0,0,128]])
        assert np.array_equal(desired, board.board)
        assert board.score == 0

    # Combining tiles

    def test_move_up_combine_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,64,0],[0,0,64,0],[0,0,0,0]]))
        board.move(Direction.UP)
        desired = np.array([[2,0,128,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.score == 128

    def test_move_down_combine_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,16,0,0],[0,16,0,0],[0,0,0,0]]))
        board.move(Direction.DOWN)
        desired = np.array([[2,0,0,0],[0,0,0,0],[0,0,0,0],[0,32,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.score == 32

    def test_move_left_combine_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,2,2]]))
        board.move(Direction.LEFT)
        desired = np.array([[2,0,0,0],[0,0,0,0],[0,0,0,0],[4,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.score == 4

    def test_move_right_combine_tiles(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,512,512,0],[0,0,0,0],[0,0,0,0]]))
        board.move(Direction.RIGHT)
        desired = np.array([[2,0,0,0],[0,0,0,1024],[0,0,0,0],[0,0,0,0]])
        assert np.array_equal(desired, board.board)
        assert board.score == 1024

    # Win and Lose states

    def test_move_win(self):
        board = Board(123, initial=np.array([[0,0,0,0],[0,0,1024,0],[0,0,1024,0],[0,0,0,0]]))
        board.move(Direction.DOWN)
        desired = np.array([[2,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,2048,0]])
        assert np.array_equal(desired, board.board)
        assert board.state == BoardState.WON

    def test_move_loss(self):
        board = Board(123, initial=np.array([[2,4,2,4],[4,8,4,8],[8,16,8,16],[32,64,128,128]]))
        board.move(Direction.RIGHT)
        desired = np.array([[2,4,2,4],[4,8,4,8],[8,16,8,16],[2,32,64,256]])
        assert np.array_equal(desired, board.board)
        assert board.state == BoardState.LOST
