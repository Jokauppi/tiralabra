import os

from ui.quit import Quit
from ui.game import GameUI
from ui.ai_menu import AIUI
from ui.menu import Menu


class App():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.game_ui = GameUI(self.io)
        self.ai_ui = AIUI(self.io)

    def run(self):

        commands = [
            {
                "action": self.game_ui.view,
                "message": "Start game",
                "shortcut": "s"
            },
            {
                "action": self.ai_ui.view,
                "message": "AI menu",
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
