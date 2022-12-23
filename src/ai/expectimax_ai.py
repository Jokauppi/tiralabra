from copy import deepcopy
import random
import sys
from game.board_utils import Direction, BoardState
from game.board import Board


class ExpectimaxAI ():
    def __init__(self, heuristic_func="Score"):

        self.heuristic_func = self.__heuristic
        if heuristic_func != "Score":
            self.heuristic_func = heuristic_func,

        self.moves = [
            Direction.UP,
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT]

    def get_move(self, board: Board):

        best_value = -sys.maxsize
        best_move = None

        for move in self.moves:
            board_child = deepcopy(board)
            board_child.move(move, add_number=False, check_state=True)
            child_value = self.__expectimax(board_child, 3)

            if child_value > best_value:
                best_value = child_value
                best_move = move

        return best_move

    def __expectimax(self, board: Board, depth, players_turn=False):

        if depth == 0 or board.state != BoardState.INPROGRESS:
            return self.heuristic_func(board)

        if players_turn:

            a = -sys.maxsize

            for move in self.moves:
                board_child = deepcopy(board)
                board_child.move(move, add_number=False, check_state=False)

                if move != board_child.immovable_direction:
                    board_child.check_state
                    a = max(a, self.__expectimax(board_child, depth - 1))
        else:

            a = 0
            possible_numbers = board.possible_new_numbers()
            free_tiles_amount = len(possible_numbers) / 2

            for new_tile in possible_numbers:
                board_child = deepcopy(board)
                board_child.put_number(new_tile[0], new_tile[1])
                board_child.check_state()
                a = a + (1.0 / free_tiles_amount * \
                         new_tile[2] * self.__expectimax(board_child, depth - 1, players_turn=True))

        return a

    def __heuristic(self, board: Board):
        if board.state == BoardState.LOST:
            return 0
        elif BoardState == BoardState.WON:
            return board.score * 2
        return board.score
