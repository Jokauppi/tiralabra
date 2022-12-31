"""Runs a game algorithm in benchmark mode."""
import threading
import random
import time
from datetime import timedelta
from collections import Counter
from game.board_utils import BoardState
from game.board import Board
from ui.algorithm_menu import AlgorithmMenu


class AIBenchmark():
    """
    Class for running a game algorithm without printing.
    The games are timed and a summary of game statistics is shown.
    Asks how many games should be run.

    Attributes
        algorithm_menu: Menu class for choosing the algorithm to use
    """

    def __init__(self):
        """Constructor for the class"""
        self.algorithm_menu = AlgorithmMenu()

    def view(self):
        """Method for starting the benchmark view"""

        ai = self.algorithm_menu.view()

        games = input("Amount of games:")
        if games == "":
            games = 1

        try:
            self.run_ai(ai, games)
        except BaseException:
            pass

    def run_ai(self, ai, game_amount):
        """
        Private method for running the chosen algorithm for the specified amount of times.

        Parameters:
            ai: Game algorithm to be run.
            game_amount (int): Amount of games to run.
        """

        game_amount = int(game_amount)
        clock = time.pthread_getcpuclockid(threading.get_ident())

        scores = []
        max_numbers = []
        wins = 0
        move_times = []
        game_times = []

        for game in range(game_amount):
            seed = random.getrandbits(24)
            game_start = time.clock_gettime_ns(clock)
            board = Board(seed)
            while board.state == BoardState.INPROGRESS:
                move_start = time.clock_gettime_ns(clock)
                move = ai.get_move(board)
                move_end = time.clock_gettime_ns(clock)
                board.move(move)
                move_times.append(move_end - move_start)
            if board.state == BoardState.LOST:
                print("Game " + str(game) + ": LOST")
            else:
                game_end = time.clock_gettime_ns(clock)
                game_times.append(game_end - game_start)
                wins += 1
                print("Game " + str(game) + ": WON")
                while board.state != BoardState.LOST:
                    move_start = time.clock_gettime_ns(clock)
                    move = ai.get_move(board)
                    move_end = time.clock_gettime_ns(clock)
                    board.move(move)
                    move_times.append(move_end - move_start)
            scores.append(board.score)
            max_numbers.append(board.get_max_number())

        max_numbers.sort()

        try:
            avg_victory_time = str(
                timedelta(
                    microseconds=(
                        (sum(game_times) / len(game_times)) / 1000)))
        except BaseException:
            avg_victory_time = "-"

        print(f"""
SUMMARY
=========
Wins: {wins}
Games played: {game_amount}
Win%: {wins / game_amount * 100}
Max score: {max(scores)}
Avg score: {sum(scores) / len(scores)}
Avg time per move: {str(timedelta(microseconds=((sum(move_times) / len(move_times)) / 1000)))}
Avg time to victory: {avg_victory_time}
Max highest number: {max(max_numbers)}
Median highest number: {max_numbers[len(max_numbers) // 2]}
        """)

        max_number_occurrences = Counter(max_numbers)
        print("=========\nHIGHEST NUMBERS OCCURRENCES")
        for number in list(max_number_occurrences):
            print((str(number) + ":").ljust(7) +
                  max_number_occurrences[number] * "*")
