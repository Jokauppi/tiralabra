
from game.board import Board
from game.board_utils import BoardState
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
            self.run_ai(self.menu.show(ai_choices))
        except:
            pass

    def run_ai(ai):
        seed = random.getrandbits(32)
        print("Seed: " + seed)
        board = Board(seed)
        while board.state != BoardState.INPROGRESS:
            board.move(ai.get_move(board))
        if board.state == BoardState.WON:
            print(board)
            print("Board won!")
        else:
            print(board)
            print("Board lost!")