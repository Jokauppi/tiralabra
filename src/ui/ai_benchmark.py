
from game.board import Board
from ui.menu import Menu


class AIBenchmark():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)

    def view(self):
        commands = [
            {
                "action": lambda *args: None,
                "message": "noop",
                "shortcut": "n"
            }
        ]

        try:
            self.menu.show(commands)()
        except BaseException:
            pass
