"""Menu for choosing a seed or generating a random one."""
import random
from ui.menu import Menu


class SeedUI():
    """
    Class for for choosing a seed for the game

    Attributes:
        menu (Menu): General menu class to show the seed menu.
    """

    def __init__(self):
        """Constructor for the class"""
        self.menu = Menu()

    def view(self):
        """
        Ask if the user wants to specify a seed number

        Returns:
            int: The seed number.
        """

        commands = [
            {
                "action": self.rand_seed,
                "message": "Random seed",
                "shortcut": "r"
            },
            {
                "action": self.ask_seed,
                "message": "Choose seed",
                "shortcut": "s"
            }
        ]

        seed = self.menu.show(commands, "Select seed", cancel=False)()
        print("the seed is: " + str(seed))
        return seed

    def ask_seed(self):
        """
        Prompt the user for a seed number

        Returns:
            int: The seed number.
        """
        return input("Input a seed: ")

    def rand_seed(self):
        """
        Generate a random seed

        Returns:
            int: The seed number.
        """
        return random.getrandbits(24)
