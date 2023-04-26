import chess as ch
import chess.svg as svg

def make_board():
    board = ch.Board()
    boardgui = svg.board(board=board)
    return board

def show_board(board):
    boardgui = svg.board(board=board)
    return boardgui

def is_valid(board):
    if (board.is_valid() and 
        not board.is_checkmate() and 
        not board.is_stalemate() and 
        not board.is_insufficient_material() and 
        not board.is_seventyfive_moves() and 
        not board.is_fivefold_repetition()):
        return True
        

def board_update(board, move):
    todo = ch.Move.from_uci(move)
    board.push(todo)
    return board

def board_reset(board):
    board.reset()

def board_undo(board):
    board.pop()


