"""User playable view of the game"""
from os import getenv
from ui.quit import Quit
from ui.seed import SeedUI
from ui.menu import Menu
from game.board import Board
from game.board_utils import Utils, BoardState, Direction


class GameUI():
    """
    Class for manually playing the game.

    Attributes:
        menu (Menu): General menu class for supplying the moves.
        seed_ui: Menu for asking for the seed.
    """

    def __init__(self):
        """Constructor for the class"""
        self.menu = Menu()
        self.seed_ui = SeedUI()
        self.utils = Utils()

    def view(self):
        """Method to start the game"""
        seed = self.seed_ui.view()
        size = getenv("BOARD_SIZE")
        if not size:
            size = 4
        board = Board(seed, int(size))
        print(self.utils.board_to_string(board))

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
                    print(self.utils.board_to_string(board, redraw=True))
                    if board.state == BoardState.LOST:
                        print("GAME LOST!")
                        self.__quit_game()
                    elif board.state == BoardState.WON:
                        print("GAME WON!")
                        self.__quit_game()
            except Quit:
                break

    def __quit_game(self):
        """Quit the game"""
        raise Quit
