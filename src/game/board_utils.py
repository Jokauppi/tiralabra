"""Helper functions for manipulating the game board."""
from enum import Enum
from typing import Tuple
import numpy.typing as npt


class Utils():
    """Class containing board utility function"""

    def __init__(self):
        """Constructor for the class"""

    def push_line(
            self, line: npt.ArrayLike) -> Tuple[npt.ArrayLike, bool, int]:
        """
        Pushes the numbers of the supplied line to the end and
        combines equal adjacent values.
        Values won't be combined to values that were
        already combined during the same push.

        Parameters:
            line (ArrayLike): line to be pushed
        """

        pointer_1 = len(line) - 2
        pointer_2 = len(line) - 1

        modified = False
        score = 0

        # pylint: disable=unsubscriptable-object, unsupported-assignment-operation

        while pointer_1 >= 0:
            if line[pointer_1] > 0 and line[pointer_2] == 0:
                line[pointer_2] = line[pointer_1]
                line[pointer_1] = 0
                pointer_1 -= 1
                modified = True
            elif line[pointer_1] == 0:
                pointer_1 -= 1
            elif line[pointer_1] == line[pointer_2]:
                line[pointer_2] *= 2
                line[pointer_1] = 0
                score += line[pointer_2]
                pointer_1 -= 1
                pointer_2 -= 1
                modified = True
            elif line[pointer_1] > 0 and line[pointer_2] > 0:
                if pointer_2 - 1 == pointer_1:
                    pointer_1 -= 1
                    pointer_2 -= 1
                else:
                    pointer_2 -= 1
            else:  # pragma: no cover
                raise Exception("unnoticed line push case")

        return (line, modified, score)

    def pull_line(
            self, line: npt.ArrayLike) -> Tuple[npt.ArrayLike, bool, int]:
        """
        Pulls the numbers of the supplied line to the end and
        combines equal adjacent values.
        Values won't be combined to values that were
        already combined during the same pull.

        Parameters:
            line (ArrayLike): line to be pulled
        """

        # pylint: disable=unsubscriptable-object, unsupported-assignment-operation

        line_end = len(line)
        pointer_1 = 0
        pointer_2 = 1

        modified = False
        score = 0

        while pointer_2 < line_end:
            if line[pointer_2] > 0 and line[pointer_1] == 0:
                line[pointer_1] = line[pointer_2]
                line[pointer_2] = 0
                pointer_2 += 1
                modified = True
            elif line[pointer_2] == 0:
                pointer_2 += 1
            elif line[pointer_1] == line[pointer_2]:
                line[pointer_1] *= 2
                line[pointer_2] = 0
                score += line[pointer_1]
                pointer_1 += 1
                pointer_2 += 1
                modified = True
            elif line[pointer_1] > 0 and line[pointer_2] > 0:
                if pointer_1 + 1 == pointer_2:
                    pointer_1 += 1
                    pointer_2 += 1
                else:
                    pointer_1 += 1
            else:
                raise Exception("unnoticed line push case")

        return (line, modified, score)

    def is_line_movable(self, line):
        """
        Checks if the supplied line is movable in either direction.

        Parameters:
            line: A row or the column of the game board.

        Returns:
            bool: whether the line is movable.
        """
        # pylint: disable=unsubscriptable-object, unsupported-assignment-operation

        for index in range(len(line) - 1):
            if line[index] == 0 or line[index] == line[index + 1]:
                return True
        return False

    def board_to_string(
            self,
            board_object,
            redraw=False,
            bottom_buffer=0,
            score=True) -> str:  # pragma: no cover
        """
        Provides a string representation of the board state and score.

        Parameters:
            board_object (Board): Board to be converted.
            redraw (bool): Whether to draw the board over the previous board.
                Allows to "update the same board" without printing a new one.
            bottom_buffer (int): Optional, default 0. Allows to rewind additional rows
                if additional lines were printed after the board.
            score (bool): Whether to print the score under the board.


        Returns:
            string: The board as a string
        """

        size = board_object.size
        board = board_object.board

        if score:
            bottom_buffer += 1

        start_line = "╔" + (size - 1) * "════╦" + "════╗\n"
        if redraw:
            start_line = (2 * size + 1 + bottom_buffer) * "\033[F" + start_line
        middle_lines = ""
        separator = "╠" + (size - 1) * "════╬" + "════╣\n"

        for index in range(size):
            row = board[index]
            number_line = "║"
            for number in row:
                if number == 0:
                    number_line += f'\33[30m{number:4d}\33[0m║'
                elif number > 64:
                    number_line += f'\33[33m{number:4d}\33[0m║'
                elif number > 4:
                    number_line += f'\33[31m{number:4d}\33[0m║'
                else:
                    number_line += f'{number:4d}║'
            number_line += "\n"
            middle_lines += number_line
            if index < size - 1:
                middle_lines += separator

        end_line = "╚" + (size - 1) * "════╩" + "════╝"

        if score:
            end_line += "\nScore: " + str(board_object.score)

        return start_line + middle_lines + end_line


class BoardState(Enum):
    """Possible states of the game board"""
    INPROGRESS = 1
    LOST = 2
    WON = 3


class Direction(Enum):
    """Possible move directions in the game."""
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
