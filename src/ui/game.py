"""User playable view of the game"""
from ui.quit import Quit
from ui.seed import SeedUI
from game.board import Board
from game.board_utils import Utils as utils
from game.board_utils import BoardState, Direction
from ui.menu import Menu


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

    def view(self):
        """Method to start the game"""
        seed = self.seed_ui.view()
        board = Board(seed)
        print(utils.board_to_string(board))

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
                    print(utils.board_to_string(board, redraw=True))
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
