import numpy as np
from src.game.board_utils import Utils as utils

class TestBoardUtilsLinePush:

    # Test number movement

    def test_line_push_no_change(self):
        initial = np.array([0,0,0,2])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(initial, pushed)

    def test_line_push_one_move(self):
        initial = np.array([0,0,2,0])
        desired = np.array([0,0,0,2])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_two_moves_no_combine(self):
        initial = np.array([0,4,2,0])
        desired = np.array([0,0,4,2])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)
    
    def test_line_push_two_moves_no_combine_space_in_between(self):
        initial = np.array([4,0,8,0])
        desired = np.array([0,0,4,8])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_no_move_one_combine(self):
        initial = np.array([0,0,2,2])
        desired = np.array([0,0,0,4])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_two_moves_one_combine(self):
        initial = np.array([4,4,0,0])
        desired = np.array([0,0,0,8])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_two_moves_one_combine(self):
        initial = np.array([4,4,0,0])
        desired = np.array([0,0,0,8])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_full_line_two_combines(self):
        initial = np.array([4,4,2,2])
        desired = np.array([0,0,8,4])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_full_line_two_combines_same_values(self):
        initial = np.array([16,16,16,16])
        desired = np.array([0,0,32,32])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_three_of_same_value_one_combine(self):
        initial = np.array([0,8,8,8])
        desired = np.array([0,0,8,16])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    def test_line_push_one_combine_two_moves(self):
        initial = np.array([16,4,8,8])
        desired = np.array([0,16,4,16])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(desired, pushed)

    # Test line modification boolean
    
    def test_line_push_not_modified(self):
        initial = np.array([0,0,0,8])
        (_, modified, _) = utils.push_line(initial)
        assert not modified
    
    def test_line_push_full_line_not_modified(self):
        initial = np.array([2,4,8,16])
        (_, modified, _) = utils.push_line(initial)
        assert not modified

    def test_line_push_one_move_modified(self):
        initial = np.array([0,0,2,0])
        (_, modified, _) = utils.push_line(initial)
        assert modified

    def test_line_push_two_moves_modified(self):
        initial = np.array([1024,4,0,0])
        (_, modified, _) = utils.push_line(initial)
        assert modified

    def test_line_push_one_combine_modified(self):
        initial = np.array([0,0,8,8])
        (_, modified, _) = utils.push_line(initial)
        assert modified

    def test_line_push_two_combines_modified(self):
        initial = np.array([2,2,4,4])
        (_, modified, _) = utils.push_line(initial)
        assert modified

    # Test line modification score

    def test_line_push_no_moves(self):
        initial = np.array([2,4,2,4])
        (_, _, score) = utils.push_line(initial)
        assert score == 0

    def test_line_push_moves_no_combines(self):
        initial = np.array([2,4,0,0])
        (_, _, score) = utils.push_line(initial)
        assert score == 0

    def test_line_one_combine(self):
        initial = np.array([8,8,0,0])
        (_, _, score) = utils.push_line(initial)
        assert score == 16

    def test_line_one_combine_one_move(self):
        initial = np.array([16,16,16,0])
        (_, _, score) = utils.push_line(initial)
        assert score == 32

    def test_line_two_combines(self):
        initial = np.array([4,4,4,4])
        (_, _, score) = utils.push_line(initial)
        assert score == 16
    
    def test_line_combine_2048(self):
        initial = np.array([0,1024,1024,0])
        (_, _, score) = utils.push_line(initial)
        assert score == 2048