import random
from ui.menu import Menu


class SeedUI():
    def __init__(self):
        self.menu = Menu()

    def view(self):

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
        return input("Input a seed: ")

    def rand_seed(self):
        return random.getrandbits(32)
