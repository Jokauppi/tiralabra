from ui.seed import SeedUI

class GameUI():
    def __init__(self, io):
        self.io = io
        self.seed_ui = SeedUI(self.io)

    def view(self):
        seed = self.seed_ui.view()
