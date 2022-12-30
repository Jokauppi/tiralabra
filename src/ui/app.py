import os

from ui.quit import Quit
from ui.game import GameUI
from ui.ai_menu import AIUI
from ui.menu import Menu


class App():
    def __init__(self):
        self.menu = Menu()
        self.game_ui = GameUI()
        self.ai_ui = AIUI()

    def run(self):

        commands = [
            {
                "action": self.ai_ui.view,
                "message": "AI play",
                "shortcut": "a"
            },
            {
                "action": self.game_ui.view,
                "message": "Manual play",
                "shortcut": "s"
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
        raise Quit
