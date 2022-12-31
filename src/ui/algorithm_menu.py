"""Menu for choosing the game algorithm to use"""
from ui.menu import Menu
from ai.random_ai import RandomAI
from ai.expectimax_ai import ExpectimaxAI


class AlgorithmMenu():
    """
    Class for choosing an algorithm to be run and for setting algorithm specific options

    menu: General menu class to display the menu.
    random_ai: Class for the random move based algorithm.
    expectimax_ai: Class for the expectimax based algorithm.
    """

    def __init__(self):
        """Constructor for the class"""
        self.menu = Menu()
        self.random_ai = RandomAI()
        self.expectimax_ai = ExpectimaxAI()

    def view(self):
        """
        Method for viewing the algorithm menu.
        Also presents a menu for chosing the algorithm heuristics and search depth if applicable.

        Returns:
            An instance of the chosen algorithm.
        """
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
