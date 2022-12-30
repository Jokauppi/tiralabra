
import threading
import random
from game.board_utils import BoardState
from game.board import Board
from ui.menu import Menu
from ui.algorithm_menu import AlgorithmMenu
from ai.random_ai import RandomAI
from ai.expectimax_ai import ExpectimaxAI
import time
from datetime import timedelta
from collections import Counter


class AIBenchmark():
    def __init__(self, io):
        self.io = io
        self.menu = Menu(self.io)
        self.algorithm_menu = AlgorithmMenu(self.io)
        self.random_ai = RandomAI()
        self.expectimax_ai = ExpectimaxAI()

    def view(self):

        ai = self.algorithm_menu.view()

        games = input("Amount of games:")
        if games == "":
            games = 1

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
            avg_victory_time = str(
                timedelta(
                    microseconds=(
                        (sum(game_times) / len(game_times)) / 1000)))
        except BaseException:
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

        max_number_occurrences = Counter(max_numbers)
        print("=========\nHIGHEST NUMBERS OCCURRENCES")
        for number in list(max_number_occurrences):
            print((str(number) + ":").ljust(7) +
                  max_number_occurrences[number] * "*")
