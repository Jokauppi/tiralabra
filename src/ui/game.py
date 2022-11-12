from ui.seed import SeedUI
from game.board import Board

class GameUI():
    def __init__(self, io):
        self.io = io
        self.seed_ui = SeedUI(self.io)

    def view(self):
        seed = self.seed_ui.view()
        #board_size = 4
        #board = Board(seed, board_size)

