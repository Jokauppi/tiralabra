import sys
from copy import copy
from game.board_utils import Direction, BoardState
from game.board import Board
import numpy as np


class ExpectimaxAI ():
    def __init__(self):

        self.heuristic_func = self.score
        self.depth = 3

        self.moves = [
            Direction.UP,
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT]
        
        self.snake_weights = np.array([[4,5,12,13],[3,6,11,14],[2,7,10,15],[1,8,9,16]])
        self.edge_weights = np.array([[100,10,10,100],[10,1,1,10],[10,1,1,10],[100,10,10,100]])

    def get_move(self, board: Board):

        best_value = -sys.maxsize
        best_move = None

        for move in self.moves:
            board_child = copy(board)
            board_child.move(move, add_number=False, check_state=False)
            
            if move != board_child.immovable_direction:
                board_child.check_state()
                child_value = self.__expectimax(board_child, self.depth)
            
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
                board_child = copy(board)
                board_child.move(move, add_number=False, check_state=False)

                if move != board_child.immovable_direction:
                    board_child.check_win()
                    a = max(a, self.__expectimax(board_child, depth - 1))
        else:

            a = 0
            possible_numbers = board.possible_new_numbers()
            free_tiles_amount = len(possible_numbers) / 2

            for new_tile in possible_numbers:
                board_child = copy(board)
                board_child.put_number(new_tile[0], new_tile[1])
                board_child.check_loss()
                a = a + (1.0 / free_tiles_amount * \
                         new_tile[2] * self.__expectimax(board_child, depth - 1, players_turn=True))

        return a

    def set_depth(self, depth):
        self.depth = depth

    def get_heuristics(self):
        return [
            {
            "action": self.snake,
            "message": "Weighed in snake pattern",
            "shortcut": "z"
            },
            {
            "action": self.score,
            "message": "Score based",
            "shortcut": "s"
            },
            {
            "action": self.edge,
            "message": "Weighed on board edges",
            "shortcut": "e"
            }
        ]
        

    def set_heuristics(self, heuristics):
        self.heuristic_func = heuristics

    def score(self, board: Board):
        if board.state == BoardState.LOST:
            return 0
        if board.state == BoardState.WON:
            return board.score * 2
        return board.score

    def snake(self, board: Board):
        if board.state == BoardState.LOST:
            return 0
        return np.sum(np.multiply(board.board, self.snake_weights))

    def edge(self, board: Board):
        if board.state == BoardState.LOST:
            return 0
        return np.sum(np.multiply(board.board, self.edge_weights))

    def snake_and_empty_space(self, board: Board):
        pass

    def edge_and_empty_space(self, board: Board):
        pass
