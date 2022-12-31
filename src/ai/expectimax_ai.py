"""Expectimax algorithm for providing moves based on the game state."""
import sys
from copy import copy
import numpy as np
from game.board_utils import Direction, BoardState
from game.board import Board


class ExpectimaxAI ():
    """
    Algorithm for providing game moves based on the expectimax algrithm and
    various simple heuristic functions.

    Attributes:
        heuristic_func: Method that provides a value for a given game state.
        depth: Search depth to be used in the algorithm.
        moves: Possible moves to be tried.
        zigzag_weights: Weight array to be used by the zigzag heuristic method.
        edge_weights: Weight array to be used by the edge heuristic method.
    """

    def __init__(self):
        """Constructor for the class"""
        self.heuristic_func = self.score
        self.depth = 3

        self.moves = [
            Direction.UP,
            Direction.RIGHT,
            Direction.DOWN,
            Direction.LEFT]

        self.zigzag_weights = np.array(
            [[4, 5, 12, 13], [3, 6, 11, 14], [2, 7, 10, 15], [1, 8, 9, 16]])
        self.edge_weights = np.array([[100, 10, 10, 100], [10, 1, 1, 10], [
                                     10, 1, 1, 10], [100, 10, 10, 100]])

    def get_move(self, board: Board):
        """
        Gives the best move according to the algorithm based on the game state.

        Parameters:
            board (Board): The current game state.

        Returns:
            Direction: Move to be made.
        """

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
        """
        Expectimax method to give value of a node at a certain depth.
        Recursively searches for possible moves and
        at the specified depth calculates the board value.
        On the players turn the value is maximized, on the computers
        turn the propabilities of possible outcomes are \"expected\".

        Parameters:
            board (Board): The board state a node.
            depth (int): The depth to search down to.
            players_turn (bool): Determines if it's the players or computers turn.

        Returns:
            float: node value
        """

        if depth == 0 or board.state == BoardState.LOST:
            return self.heuristic_func(board)

        if players_turn:

            e_max_value = -sys.maxsize

            for move in self.moves:
                board_child = copy(board)
                board_child.move(move, add_number=False, check_state=False)

                if move != board_child.immovable_direction:
                    board_child.check_win()
                    e_max_value = max(
                        e_max_value, self.__expectimax(
                            board_child, depth - 1))
        else:

            e_max_value = 0
            possible_numbers = board.possible_new_numbers()

            for new_tile in possible_numbers:
                board_child = copy(board)
                board_child.put_number(new_tile[0], new_tile[1])
                board_child.check_loss()
                e_max_value = e_max_value + (new_tile[2] * self.__expectimax(
                    board_child, depth - 1, players_turn=True))

        return e_max_value

    def set_depth(self, depth):
        """
        Sets the algorithm depth.

        Parameters:
            depth (int): Depth to be set.
        """
        self.depth = depth

    def get_heuristics(self):
        """
        Gets a list of the possible heuristic funtions and
        their descriptions and shortcuts to be used by AlgorithmMenu
        """
        return [
            {
                "action": self.zigzag,
                "message": "Weighed zigzag",
                "shortcut": "z"
            },
            {
                "action": self.corner,
                "message": "Weighed corner",
                "shortcut": "c"
            },
            {
                "action": self.score,
                "message": "Score based",
                "shortcut": "s"
            },
            {
                "action": self.edge,
                "message": "Weighed edges",
                "shortcut": "e"
            }
        ]

    def set_heuristics(self, heuristic):
        """
        Sets the heuristic method to be used by the algorithm.

        Parameters:
            heuristic: Heuristics method to be used.
        """
        self.heuristic_func = heuristic

    def score(self, board: Board):
        """
        Score based heuristic method. Prefers game states with higher scores

        Parameters:
            board (Board): The game state at a node.
        """
        if board.state == BoardState.LOST:
            return 0
        if board.state == BoardState.WON:
            return board.score * 2
        return board.score

    def zigzag(self, board: Board):
        """
        Weighed zigzag based heuristic method.
        Prefers tiles to be in a zigzag patter in decreasing order.

        Parameters:
            board (Board): The game state at a node.
        """
        if board.state == BoardState.LOST:
            return 0
        return np.sum(np.multiply(board.board, self.zigzag_weights))

    def corner(self, board: Board):
        """
        Weighed corner based heuristic method. Prefers larger tiles to be close to a single corner.

        Parameters:
            board (Board): The game state at a node.
        """
        if board.state == BoardState.LOST:
            return 0

        sum = 0
        for i in range(board.size):
            for j in range(board.size):
                sum += (i + j) * board.board[i][j]

        return sum

    def edge(self, board: Board):
        """
        Weighed edge based heuristic method. Prefers larger tiles to be on any of the corners..

        Parameters:
            board (Board): The game state at a node.
        """
        if board.state == BoardState.LOST:
            return 0
        return np.sum(np.multiply(board.board, self.edge_weights))
