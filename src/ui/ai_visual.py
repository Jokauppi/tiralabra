
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
            self.run_ai(ai)
        except BaseException as e:
            print(traceback.format_exc())

    def run_ai(self, ai):
        seed = random.getrandbits(32)
        print("Seed: " + str(seed))
        board = Board(seed)
        utils.print_board(board)
        while board.state == BoardState.INPROGRESS:
            move = ai.get_move(board)
            board.move(move)
            utils.print_board(board, redraw=True)
            sleep(0.01)
        if board.state == BoardState.WON:
            print("Board won!")
        else:
            print("Board lost!")
