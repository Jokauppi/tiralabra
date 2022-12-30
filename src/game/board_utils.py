from enum import Enum
from typing import Tuple
import numpy.typing as npt


class Utils():

    def push_line(line: npt.ArrayLike) -> Tuple[npt.ArrayLike, bool, int]:

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
            else:
                raise Exception("unnoticed line push case")

        return (line, modified, score)

    def pull_line(line: npt.ArrayLike) -> Tuple[npt.ArrayLike, bool, int]:

        # pylint: disable=unsubscriptable-object, unsupported-assignment-operation

        max = len(line)
        pointer_1 = 0
        pointer_2 = 1

        modified = False
        score = 0

        while pointer_2 < max:
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

    def is_line_movable(line):
        for index in range(len(line) - 1):
            if line[index] == 0 or line[index] == line[index + 1]:
                return True
        return False

    def board_to_string(
            board_object,
            redraw=False,
            bottom_buffer=0,
            score=True):

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
                    number_line += '\33[30m{:4d}\33[0m║'.format(number)
                elif number > 64:
                    number_line += '\33[33m{:4d}\33[0m║'.format(number)
                elif number > 4:
                    number_line += '\33[31m{:4d}\33[0m║'.format(number)
                else:
                    number_line += '{:4d}║'.format(number)
            number_line += "\n"
            middle_lines += number_line
            if index < size - 1:
                middle_lines += separator

        end_line = "╚" + (size - 1) * "════╩" + "════╝"

        if score:
            end_line += "\nScore: " + str(board_object.score)

        return start_line + middle_lines + end_line


class BoardState(Enum):
    INPROGRESS = 1
    LOST = 2
    WON = 3


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
