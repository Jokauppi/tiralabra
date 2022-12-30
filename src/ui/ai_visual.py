
from time import sleep
from game.board import Board
from game.board_utils import BoardState
from game.board_utils import Utils as utils
from ui.menu import Menu
from ui.algorithm_menu import AlgorithmMenu
from ai.random_ai import RandomAI
from ai.expectimax_ai import ExpectimaxAI
import random


class AIVisual():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.algorithm_menu = AlgorithmMenu(self.io)
        self.random_ai = RandomAI()
        self.expectimax_ai = ExpectimaxAI()

    def view(self):

        ai = self.algorithm_menu.view()

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

        speed = self.menu.show(speeds, "Choose Game Speed", cancel=False)

        self.run_ai(ai, speed)

    def run_ai(self, ai, speed):
        seed = random.getrandbits(32)
        print("Seed: " + str(seed))
        board = Board(seed, board_size=4)
        print(utils.board_to_string(board))
        while board.state == BoardState.INPROGRESS:
            move = ai.get_move(board)
            board.move(move)
            print(utils.board_to_string(board, redraw=True))
            if speed > 0:
                sleep(speed)
        if board.state == BoardState.LOST:
            print("Board lost!")
        else:
            print("Board won!")
            # Continue after win
            print("Game continued after win:")
            print(utils.board_to_string(board))
            while board.state != BoardState.LOST:
                move = ai.get_move(board)
                board.move(move)
                print(utils.board_to_string(board, redraw=True))
