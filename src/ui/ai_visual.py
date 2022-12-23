
from time import sleep
import traceback
from game.board import Board
from game.board_utils import BoardState
from game.board_utils import Utils as utils
from ui.menu import Menu
from ai.random_ai import RandomAI
from ai.expectimax_ai import ExpectimaxAI
import random


class AIVisual():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.random_ai = RandomAI()
        self.expectimax_ai = ExpectimaxAI()

    def view(self):
        ai_choices = [
            {
                "action": self.expectimax_ai,
                "message": "Expectimax algorithm",
                "shortcut": "e"
            },
            {
                "action": self.random_ai,
                "message": "Random moves",
                "shortcut": "r"
            }
        ]

        try:
            ai = self.menu.show(ai_choices, "Choose algorithm",cancel=False)
        except BaseException as e:
            print(traceback.format_exc())

        speeds = [
            {
                "action": 0,
                "message": "no pause",
                "shortcut": "1"
            },
            {
                "action": 0.02,
                "message": "0.2 ms pause",
                "shortcut": "2"
            },
            {
                "action": 1,
                "message": "1 s pause between moves",
                "shortcut": "3"
            }
        ]

        try:
            speed = self.menu.show(speeds, "Choose Game Speed",cancel=False)
        except BaseException as e:
            print(traceback.format_exc())

        if hasattr(ai, "set_heuristics"):
            try:
                heuristics = self.menu.show(ai.get_heuristics(), "Choose Heuristics", cancel=False)
                ai.set_heuristics(heuristics)
            except BaseException as e:
                print(traceback.format_exc())

        if hasattr(ai, "set_depth"):
            depth = input("Set algorithm search depth [empty = 3]: ")
            if depth == "":
                ai.set_depth(3)
            else:
                ai.set_depth(int(depth))

        self.run_ai(ai, speed)

    def run_ai(self, ai, speed):
        seed = random.getrandbits(32)
        print("Seed: " + str(seed))
        board = Board(seed, board_size=4)
        utils.print_board(board)
        while board.state == BoardState.INPROGRESS:
            move = ai.get_move(board)
            board.move(move)
            utils.print_board(board, redraw=True)
            if speed > 0:
                sleep(speed)
        if board.state == BoardState.LOST:
            print("Board lost!")
        else:
            print("Board won!")
            # Continue after win
            print("Game continued after win:")
            utils.print_board(board)
            while board.state != BoardState.LOST:
                move = ai.get_move(board)
                board.move(move)
                utils.print_board(board, redraw=True)
        
