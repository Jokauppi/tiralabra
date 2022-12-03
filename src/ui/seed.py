import random
from ui.menu import Menu


class SeedUI():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)

    def view(self):

        commands = [
            {
                "action": self.ask_seed,
                "message": "Choose seed",
                "shortcut": "s"
            },
            {
                "action": self.rand_seed,
                "message": "Random seed",
                "shortcut": "r"
            }
        ]

        seed = self.menu.show(commands, "Select seed", cancel=False)()
        print("the seed is: " + str(seed))
        return seed

    def ask_seed(self):
        return self.io.input("Input a seed: ")

    def rand_seed(self):
        return random.getrandbits(32)
