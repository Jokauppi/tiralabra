
from time import sleep
import traceback
from game.board import Board
from game.board_utils import BoardState
from game.board_utils import Utils as utils
from ui.menu import Menu
from ai.random_ai import RandomAI
import random


class AIVisual():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.random_ai = RandomAI()

    def view(self):
        ai_choices = [
            {
                "action": self.random_ai,
                "message": "Random moves",
                "shortcut": "r"
            }
        ]

        try:
            ai = self.menu.show(ai_choices, cancel=False)
        except BaseException as e:
            print(traceback.format_exc())

        speeds = [
            {
                "action": 1,
                "message": "slow",
                "shortcut": "1"
            },
            {
                "action": 0.02,
                "message": "fast",
                "shortcut": "2"
            },
            {
                "action": 0,
                "message": "instant",
                "shortcut": "3"
            }
        ]

        try:
            speed = self.menu.show(speeds, cancel=False)
        except BaseException as e:
            print(traceback.format_exc())

        self.run_ai(ai, speed)

    def run_ai(self, ai, speed):
        seed = random.getrandbits(32)
        print("Seed: " + str(seed))
        board = Board(seed)
        utils.print_board(board)
        while board.state == BoardState.INPROGRESS:
            move = ai.get_move(board)
            board.move(move)
            utils.print_board(board, redraw=True)
            if speed > 0:
                sleep(speed)
        if board.state == BoardState.WON:
            print("Board won!")
        else:
            print("Board lost!")
