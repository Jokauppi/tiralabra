"""The main application class"""

from ui.quit import Quit
from ui.game import GameUI
from ui.ai_menu import AIUI
from ui.menu import Menu


class App():
    """
    The main program loop

    Attributes:
        menu (Menu): General menu class to choose between game modes.
        game_ui: UI class for playing the game.
        ai_ui: Menu class to choose between the algorithm views.
    """

    def __init__(self):
        """Constructor for the class"""
        self.menu = Menu()
        self.game_ui = GameUI()
        self.ai_ui = AIUI()

    def run(self):
        """Menu for running the algorithm or pleying the game."""

        commands = [
            {
                "action": self.ai_ui.view,
                "message": "Algorithm play",
                "shortcut": "a"
            },
            {
                "action": self.game_ui.view,
                "message": "Human play",
                "shortcut": "h"
            },
            {
                "action": self.quit_program,
                "message": "Quit",
                "shortcut": "q"
            }
        ]

        while True:
            try:
                self.menu.show(commands, "2048-AI", cancel=False)()
            except Quit:
                break

    def quit_program(self):
        """Quit the program loop"""
        raise Quit
