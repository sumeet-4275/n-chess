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
        self.whiteToMove = True
        self.moveLog = []

class Move():

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptued = board[self.endRow][self.endCol]
