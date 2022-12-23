from enum import Enum


class Utils():
    def __init__(self):
        pass

    def move_line_forwards(line):

        p1 = len(line) - 2
        p2 = len(line) - 1

        modified = False
        score = 0

        while p1 >= 0:
            if line[p1] > 0 and line[p2] == 0:
                line[p2] = line[p1]
                line[p1] = 0
                p1 -= 1
                modified = True
            elif line[p1] == 0:
                p1 -= 1
            elif line[p1] == line[p2]:
                line[p2] *= 2
                line[p1] = 0
                score += line[p2]
                p1 -= 1
                p2 -= 1
                modified = True
            elif line[p1] > 0 and line[p2] > 0:
                if p2 - 1 == p1:
                    p1 -= 1
                    p2 -= 1
                else:
                    p2 -= 1
            else:
                raise Exception("unnoticed line push case")

        return (line, modified, score)

    def move_line_backwards(line):

        max = len(line)
        p1 = 0
        p2 = 1

        modified = False
        score = 0

        while p2 < max:
            if line[p2] > 0 and line[p1] == 0:
                line[p1] = line[p2]
                line[p2] = 0
                p2 += 1
                modified = True
            elif line[p2] == 0:
                p2 += 1
            elif line[p1] == line[p2]:
                line[p1] *= 2
                line[p2] = 0
                score += line[p1]
                p1 += 1
                p2 += 1
                modified = True
            elif line[p1] > 0 and line[p2] > 0:
                if p1 + 1 == p2:
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1
            else:
                raise Exception("unnoticed line push case")

        return (line, modified, score)

    def is_line_movable(line):
        for index in range(len(line) - 1):
            if line[index] == 0 or line[index] == line[index + 1]:
                return True
        return False

    def print_board(board_object, redraw=False, bottom_buffer=0, score=True):

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

        print(start_line + middle_lines + end_line)


class BoardState(Enum):
    INPROGRESS = 1
    LOST = 2
    WON = 3


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
