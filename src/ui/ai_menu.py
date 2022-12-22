
from game.board import Board
from ui.menu import Menu
from ui.ai_benchmark import AIBenchmark
from ui.ai_visual import AIVisual


class AIUI():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.ai_visual = AIVisual(self.io)

    def view(self):
        commands = [
            {
                "action": self.ai_visual,
                "message": "Visual playthrough",
                "shortcut": "v"
            }
        ]

        try:
            self.menu.show(commands).view()
        except BaseException:
            pass
