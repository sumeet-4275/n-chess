'''
This file is for maintaining the state of chess board, keeping the move logs, and taking and processing users input
'''
import numpy as np

class state():
    def __init__(self):
        self.board = np.array(
            [
                ["bR", "bN", "bB", "bQ", "bK",  "bB", "bN", "bR"],
                ["bp", "bp", "bp", "bp", "bp",  "bp", "bp", "bp"],
                ["--", "--", "--", "--", "--",  "--", "--", "--"],
                ["--", "--", "--", "--", "--",  "--", "--", "--"],
                ["--", "--", "--", "--", "--",  "--", "--", "--"],
                ["--", "--", "--", "--", "--",  "--", "--", "--"],
                ["wp", "wp", "wp", "wp", "wp",  "wp", "wp", "wp"],
                ["wR", "wN", "wB", "wQ", "wK",  "wB", "wN", "wR"]
            ]
        )