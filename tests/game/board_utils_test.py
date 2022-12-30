import numpy as np
from src.game.board_utils import Utils as utils

class TestBoardUtilsLinePush:

    # Tests for number movement

    def test_line_push_no_change(self):
        initial = np.array([0,0,0,2])
        (pushed, _, _) = utils.push_line(initial)
        assert np.array_equal(initial, pushed)

    # Tests for line modification boolean
    
    # Tests for line modification score
