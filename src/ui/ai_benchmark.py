
import threading
import traceback
import random
from game.board_utils import Utils as utils
from game.board_utils import BoardState
from game.board import Board
from ui.menu import Menu
from ai.random_ai import RandomAI
from ai.expectimax_ai import ExpectimaxAI
import time
from datetime import timedelta


class AIBenchmark():
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

        try:
            ai = self.menu.show(ai_choices, "Choose algorithm", cancel=False)
            games = input("Amount of games:")
        except BaseException as e:
            print(traceback.format_exc())

        if hasattr(ai, "set_heuristics"):
            try:
                heuristics = self.menu.show(ai.get_heuristics(), "Choose heuristics", cancel=False)
                ai.set_heuristics(heuristics)
            except BaseException as e:
                print(traceback.format_exc())

        if hasattr(ai, "set_depth"):
            depth = input("Set algorithm search depth [empty = 3]: ")
            if depth == "":
                ai.set_depth(3)
            else:
                ai.set_depth(int(depth))

        self.run_ai(ai, games)

    def run_ai(self, ai, game_amount):

        game_amount = int(game_amount)
        clock = time.pthread_getcpuclockid(threading.get_ident())

        scores = []
        max_numbers = []
        wins = 0
        move_times = []
        game_times = []

        for game in range(game_amount):
            seed = random.getrandbits(32)
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
            avg_victory_time = str(timedelta(microseconds=((sum(game_times) / len(game_times)) / 1000)))
        except:
            avg_victory_time = "-"

        print("""
SUMMARY
=========
Wins: {wins}
Games played: {played}
Win%: {win_percent}
Max score: {max_score}
Avg score: {avg_score}
Avg time per move: {move_time}
Avg time to victory: {avg_victory_time}
Max highest number: {max_number}
Median highest number: {med_number}
        """.format(
            wins=wins,
            played=game_amount,
            win_percent=wins / game_amount * 100,
            max_score=max(scores),
            avg_score=sum(scores) / len(scores),
            move_time=str(timedelta(microseconds=((sum(move_times) / len(move_times)) / 1000))),
            avg_victory_time=avg_victory_time,
            max_number=max(max_numbers),
            med_number=max_numbers[len(max_numbers) // 2]
        ))

        