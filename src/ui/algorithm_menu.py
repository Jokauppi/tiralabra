
from ui.menu import Menu
from ai.random_ai import RandomAI
from ai.expectimax_ai import ExpectimaxAI


class AlgorithmMenu():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.random_ai = RandomAI()
        self.expectimax_ai = ExpectimaxAI()

    def view(self):
        ai_choices = [
            {
                "action": self.expectimax_ai,
                "message": "Expectimax algorithm",
                "shortcut": "e"
            },
            {
                "action": self.random_ai,
                "message": "Random moves",
                "shortcut": "r"
            }
        ]

        ai = self.menu.show(ai_choices, "Choose algorithm", cancel=False)

        if hasattr(ai, "set_heuristics"):
            heuristics = self.menu.show(
                ai.get_heuristics(), "Choose heuristics", cancel=False)
            ai.set_heuristics(heuristics)

        if hasattr(ai, "set_depth"):
            depth = input("Set algorithm search depth [empty = 3]: ")
            if depth == "":
                ai.set_depth(3)
            else:
                ai.set_depth(int(depth))

        return ai
