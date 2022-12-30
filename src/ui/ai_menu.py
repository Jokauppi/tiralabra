"""Menu for choosing the algorithm testing view."""
from ui.menu import Menu
from ui.ai_benchmark import AIBenchmark
from ui.ai_visual import AIVisual


class AIUI():
    """
    Opens menu for choosing a mode to test the included game algorithms.
    Included modes are a visual mode with every move printed and
    a benchmarking for measuring algorithm success rate and performance.

    Attributes:
        menu: class to display the menu
        ai_visual: class to start the visual mode
        ai_benchmark: class to start the benchmark mode

    """

    def __init__(self):
        """
        Constructor for the menu
        """
        self.menu = Menu()
        self.ai_visual = AIVisual()
        self.ai_benchmark = AIBenchmark()

    def view(self):
        """Show menu. Opens the chosen view."""
        commands = [
            {
                "action": self.ai_visual,
                "message": "Visual playthrough",
                "shortcut": "v"
            },
            {
                "action": self.ai_benchmark,
                "message": "AI benchmarking",
                "shortcut": "a"
            }
        ]

        try:
            self.menu.show(commands).view()
        except BaseException:
            pass
