"""Stores the game state"""

import random
from math import floor
import numpy as np
from game.board_utils import Utils, BoardState, Direction


class Board():
    """
    Game board class for storing the game state with
    methods for manipulating and examining it.

    Attributes:
        seed (int): Seed number for generating random new tiles.
        size (int): Size of the game board as length of the board side
        board (NDArray/ArrayLike): The state of the board tiles.
        state (BoardState): Enum which signifies whether the game is in progress, won or lost.
        score (int): The score of the game state.
        last_move (Direction): The last move the player made.
        immovable_direction (Direction): The last move the player made if the last move
            resulted in no changes on the board. Otherwise None.
            Making this move next would not change the board state.
            Can be used in algorithms to prevent checking unneccessary moves.
        winning_number (int): The number needed to win the game based on the board size
            Larger boards require larger numbers since there is more space to construct them.
    """

    def __init__(
            self,
            seed: int,
            board_size: int = 4,
            initial=None,
            score=0,
            set_seed=True):
        """
        Constructor for the class

        Parameters:
            seed (int): Seed number for generating random new tiles.
            board_size (int): Size of the game board as length of the board side.
                Optional, default is 4.
            initial (NDArray/ArrayLike): The initial state of the board tiles.
                Optional, if no initial state is supplied,
                two random tiles are added to an empty board.
            score (int): Sets the score of the game state. Optional, default if 0.
            set_seed (bool): Determines if the seed should be set when
                creating a new board state.
                Used to prevent the seed being set every tim
                a copy is made of the state e.g. in an algorithm.
        """
        self.utils = Utils()

        self.seed = int(seed)
        if set_seed:
            random.seed(self.seed)
        self.size = board_size
        if initial is None:
            self.board = np.zeros((self.size, self.size), dtype=int)
            self.__add_number()
            self.__add_number()
        else:
            self.board = initial
        self.state = BoardState.INPROGRESS
        self.score = score
        self.last_move = None
        self.immovable_direction = None
        self.winning_number = 2**(floor((10 * (self.size**2)) / 16) + 1)

    def move(self, direction: Direction, add_number=True, check_state=True):
        """
        Moves the board in the supplied direction.
        Sets the score and game state accordingly and makes a random counter-move.

        Parameters:
            Direction (Direction): Direction to move.
            add_number (bool): Optional, default True.
                If True, the move leaves the board on the computers turn
                without making a counter-move.
            check_state (bool): Optional, default True.
                Can be used to prevent checking win or loss.
                Useful in algorithms when only the other needs to be checked on one turn or
                it is convenient to check the state externally.
        """
        modified = False
        move_score = 0

        for line in range(self.size):

            if direction in (Direction.UP, Direction.DOWN):

                old_line = self.__get_column(line)

                if direction == Direction.UP:
                    (new_line, line_modified,
                     line_score) = self.utils.pull_line(old_line)
                else:
                    (new_line, line_modified,
                     line_score) = self.utils.push_line(old_line)

                if line_modified:
                    self.__set_column(line, new_line)
                    modified = True

                move_score += line_score

            else:
                old_line = self.__get_row(line)

                if direction == Direction.LEFT:
                    (new_line, line_modified,
                     line_score) = self.utils.pull_line(old_line)
                else:
                    (new_line, line_modified,
                     line_score) = self.utils.push_line(old_line)

                if line_modified:
                    self.__set_row(line, new_line)
                    modified = True

                move_score += line_score

        if modified:
            if add_number:
                self.__add_number()
            self.immovable_direction = None
        else:
            self.immovable_direction = direction

        if check_state:
            self.check_state()

        self.last_move = direction
        self.score += move_score

    def check_state(self):
        """Checks whether the game is won or lost and sets the state attribute accordingly."""
        self.check_win()
        self.check_loss()

    def set_state(self, state: BoardState):
        """
        Sets the value of the state attribute.

        Parameters:
            state (BoardState): State to be set.
        """
        self.state = state

    def check_win(self):
        """Checks whether the game is won and sets the state attribute accordingly."""
        if np.count_nonzero(self.board == self.winning_number):
            self.state = BoardState.WON

    def check_loss(self):
        """Checks whether the game is lost and sets the state attribute accordingly."""
        for row in range(self.size):
            line = self.__get_row(row)
            if self.utils.is_line_movable(line):
                return
        for col in range(self.size):
            line = self.__get_column(col)
            if self.utils.is_line_movable(line):
                return
        self.state = BoardState.LOST

    def put_number(self, tile, number):
        """
        Puts the supplied number in a the supplied position on the board.

        Parameters:
            tile (tuple): The coordinate of the tile to be set.
            number (int): The number to be set.
        """
        self.board[tile[0]][tile[1]] = number

    def empty_tiles(self):
        """
        Gets a list of coordinates of all the empty tiles on the board.

        Returns: List of tuples of the coordinates.
        """
        return np.argwhere(self.board == 0)

    def possible_new_numbers(self):
        """
        Gets a list of all possible computer moves on the board and the specific moves probability.
        Should only be use after making a move with add_number set to false.

        Returns: List of possible moves.
        """
        empty_tiles = self.empty_tiles()
        empty_tiles_amount = len(empty_tiles)
        probability_2 = 1.0 / empty_tiles_amount * 0.9
        probability_4 = 1.0 / empty_tiles_amount * 0.1

        moves = []
        for tile in empty_tiles:
            moves.append((tile, 2, probability_2))
            moves.append((tile, 4, probability_4))
        return moves

    def get_size(self):
        """
        Gets the size of the board.

        Returns: the size attribute.
        """
        return self.size

    def __add_number(self):
        """
        Adds a new number to a random empty tile.
        The number has a 90% chance of being a 2 and a 10% chance of being a 4
        """
        empty_tiles = self.empty_tiles()
        chosen_tile = empty_tiles[random.randrange(len(empty_tiles))]
        new_number = 2
        if random.randrange(10) == 0:
            new_number = 4
        self.board[chosen_tile[0]][chosen_tile[1]] = new_number

    def get_max_number(self):
        """Gets the value of the largest number on the board"""
        return np.amax(self.board)

    def __get_row(self, index):
        """
        Gets the row of the board with the spcified index:

        Parameters:
            index (int): index of row to get, counting from top to bottom.

        Returns:
            NDArray/Arraylike: the requested row
        """
        return self.board[index, :]

    def __get_column(self, index):
        """
        Gets the column of the board with the spcified index:

        Parameters:
            index (int): index of column to get, counting from left to right.

        Returns:
            NDArray/Arraylike: the requested column
        """
        return self.board[:, index]

    def __set_row(self, index, values):
        """
        Sets the row of the board with the spcified index to be the specified array:

        Parameters:
            index (int): index of row to set.
            values (NDArray/arraylike): the new row of tiles.
        """
        self.board[index, :] = values

    def __set_column(self, index, values):
        """
        Sets the column of the board with the spcified index to be the specified array:

        Parameters:
            index (int): index of column to set.
            values (NDArray/arraylike): the new column of tiles.
        """
        self.board[:, index] = values

    def __str__(self) -> str:
        # pylint: disable=invalid-str-returned
        """Gets the string representation of the board."""
        str(self.utils.board_to_string(self))

    def __copy__(self):
        """Creates a copy of the board instance. The seed is not reset."""
        new_board = Board(
            self.seed,
            self.size,
            initial=self.board.copy(),
            score=self.score,
            set_seed=False)
        new_board.last_move = self.last_move
        new_board.immovable_direction = self.immovable_direction
        return new_board
