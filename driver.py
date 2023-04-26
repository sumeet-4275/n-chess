import board_functions as bf
#import engine

def player_vs_player(board):
    bf.board_reset(board)
    return bf.show_board(board)
    while bf.is_valid(board):
        print('''
            Enter Move: 
            ''')
        move = input()
        board = bf.board_update(board, move)
        # print svg board
        svgboard = bf.show_board(board)
        return svgboard
        

def player_vs_computer():
    pass

def computer_vs_computer():
    pass

def main():
    board = bf.make_board()
    #engine.make_engine()

    print('''
        Enter Game Type: 
          1. Player vs Player
          2. Player vs Computer
          3. Computer vs Computer
          ''')
    game_type = input()
    if game_type == '1':
        player_vs_player(board)
    elif game_type == '2':
        player_vs_computer(board)
    elif game_type == '3':
        computer_vs_computer(board)
