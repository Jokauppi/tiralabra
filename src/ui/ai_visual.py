"""Runs a game algorithm in visual mode."""
from time import sleep
from game.board import Board
from game.board_utils import BoardState
from game.board_utils import Utils as utils
from ui.menu import Menu
from ui.algorithm_menu import AlgorithmMenu
import random


class AIVisual():
    """
    Class for running a game algorithm with visual moves.
    Shows a menu for slowing down the game for inspecting the moves.

    Attributes
        menu: General menu class for showing the speed menu
        algorithm_menu: Menu class for choosing the algorithm to use
    """

    def __init__(self):
        """Constructor for the class."""
        self.menu = Menu()
        self.algorithm_menu = AlgorithmMenu()

    def view(self):
        """Method for starting the visual view"""
        ai = self.algorithm_menu.view()

        speeds = [
            {
                "action": 0,
                "message": "no pause",
                "shortcut": "1"
            },
            {
                "action": 0.02,
                "message": "0.2 ms pause",
                "shortcut": "2"
            },
            {
                "action": 1,
                "message": "1 s pause between moves",
                "shortcut": "3"
            }
        ]

        speed = self.menu.show(speeds, "Choose Game Speed", cancel=False)

        try:
            self.__run_ai(ai, speed)
        except BaseException:
            pass

    def __run_ai(self, ai, speed):
        """
        Private method for running the chosen algorithm

        Parameters:
            ai: Game algorithm to be run.
            speed (float,int): Additional time to wait between moves in seconds.
        """
        seed = random.getrandbits(32)
        print("Seed: " + str(seed))
        board = Board(seed, board_size=4)
        print(utils.board_to_string(board))
        while board.state == BoardState.INPROGRESS:
            move = ai.get_move(board)
            board.move(move)
            print(utils.board_to_string(board, redraw=True))
            if speed > 0:
                sleep(speed)
        if board.state == BoardState.LOST:
            print("Board lost!")
        else:
            print("Board won!")
            # Continue after win
            print("Game continued after win:")
            print(utils.board_to_string(board))
            while board.state != BoardState.LOST:
                move = ai.get_move(board)
                board.move(move)
                print(utils.board_to_string(board, redraw=True))
