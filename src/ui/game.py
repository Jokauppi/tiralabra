
from ui.quit import Quit
from ui.seed import SeedUI
from game.board import Board
from game.board_utils import Utils as utils
from game.board_utils import Direction
from ui.menu import Menu


class GameUI():
    def __init__(self, io):
        self.io = io
        self.seed_ui = SeedUI(self.io)
        self.menu = Menu(self.io)

    def view(self):
        seed = self.seed_ui.view()
        board_size = 4
        board = Board(seed, board_size)
        utils.print_board(board.board, board_size)

        commands = [
            {
                "action": Direction.UP,
                "message": "↑",
                "shortcut": "w"
            },
            {
                "action": Direction.DOWN,
                "message": "↓",
                "shortcut": "s"
            },
            {
                "action": Direction.LEFT,
                "message": "←",
                "shortcut": "a"
            },
            {
                "action": Direction.RIGHT,
                "message": "→",
                "shortcut": "d"
            },
            {
                "action": self.__quit_game,
                "message": "Quit game",
                "shortcut": "q"
            }
        ]

        while True:
            try:
                command = self.menu.show(commands, cancel=False)
                if callable(command):
                    command()
                else:
                    board.move(command)
                utils.print_board(board.board, board_size, redraw=True)
            except Quit:
                break

    def __quit_game(self):
        raise Quit
