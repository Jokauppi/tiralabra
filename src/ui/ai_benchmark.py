
import threading
import traceback
import random
from game.board_utils import Utils as utils
from game.board_utils import BoardState
from game.board import Board
from ui.menu import Menu
from ai.random_ai import RandomAI
import time


class AIBenchmark():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.random_ai = RandomAI()

    def view(self):
        ai_choices = [
            {
                "action": self.random_ai,
                "message": "Random moves",
                "shortcut": "r"
            }
        ]

        try:
            ai = self.menu.show(ai_choices, cancel=False)
            games = input("Amount of games:")
            self.run_ai(ai, games)
        except BaseException as e:
            print(traceback.format_exc())

    def run_ai(self, ai, game_amount):

        game_amount = int(game_amount)
        clock = time.pthread_getcpuclockid(threading.get_ident())

        scores = []
        numbers = []
        wins = 0
        times = []

        for game in range(game_amount):
            seed = random.getrandbits(32)
            board = Board(seed)
            while board.state == BoardState.INPROGRESS:
                move_start = time.clock_gettime_ns(clock)
                move = ai.get_move(board)
                move_end = time.clock_gettime_ns(clock)
                board.move(move)
                times.append(move_end - move_start)
            if board.state == BoardState.WON:
                wins += 1
            scores.append(board.score)
            numbers.append(board.get_max_number())

        numbers.sort()

        print("""
SUMMARY
=========
Wins: {wins}
Games played: {played}
Win%: {win_percent}
Max score: {max_score}
Avg score: {avg_score}
Avg time per move: {move_time} μs
Max highest number: {max_number}
Median highest number: {med_number}
        """.format(
            wins=wins,
            played=game_amount,
            win_percent=wins / game_amount,
            max_score=max(scores),
            avg_score=sum(scores) / len(scores),
            move_time="{:.2f}".format((sum(times) / len(times)) / 1000),
            max_number=max(numbers),
            med_number=numbers[len(numbers) // 2]
        ))
