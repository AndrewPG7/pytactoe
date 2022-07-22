from os import system, name
from keyboard import is_pressed
from dumb_bot import DumbBot
from smart_bot import SmartBot
from time import sleep

X = 'X'
O = 'O'
const_game_end = False
const_winner = False
const_player_x_turn = True

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class Board:
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def draw_board(self):
        clear()
        print()
        for i in range(self.rows):
            print(' ', self.board[i][0], '|', self.board[i][1], '|', self.board[i][2], ' ')
            if i != 2:
                print('-------------')
        print()

    def write_on_board(self, symb, i, j):
        self.board[i][j] = symb

    def check_tile(self, i, j):
        if self.board[i][j] == '-':
            return True
        else:
            return False

    def check_win(self, symb):
        for i in range(self.rows):
            if self.board[i][0] == symb and self.board[i][1] == symb and self.board[i][2] == symb:
                return True
        for j in range(self.columns):
            if self.board[0][j] == symb and self.board[1][j] == symb and self.board[2][j] == symb:
                return True
        if self.board[0][0] == symb and self.board[1][1] == symb and self.board[2][2] == symb:
            return True
        if self.board[0][2] == symb and self.board[1][1] == symb and self.board[2][0] == symb:
            return True
        return False

    def check_ending_state(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == '-':
                    return False
        return True


def player_input(turn, board):
    if turn:
        symb = X
    else:
        symb = O
    correct_input = False
    while not correct_input:
        correct_input = True
        char = input('Input a number between 1-9 and press ENTER to confirm: ')
        if (char == '1') and board.check_tile(2, 0):
            board.write_on_board(symb, 2, 0)
        elif (char == '2') and board.check_tile(2, 1):
            board.write_on_board(symb, 2, 1)
        elif (char == '3') and board.check_tile(2, 2):
            board.write_on_board(symb, 2, 2)
        elif (char == '4') and board.check_tile(1, 0):
            board.write_on_board(symb, 1, 0)
        elif (char == '5') and board.check_tile(1, 1):
            board.write_on_board(symb, 1, 1)
        elif (char == '6') and board.check_tile(1, 2):
            board.write_on_board(symb, 1, 2)
        elif (char == '7') and board.check_tile(0, 0):
            board.write_on_board(symb, 0, 0)
        elif (char == '8') and board.check_tile(0, 1):
            board.write_on_board(symb, 0, 1)
        elif (char == '9') and board.check_tile(0, 2):
            board.write_on_board(symb, 0, 2)
        else:
            correct_input = False


def declare_winner(name, winner):
    if winner:
        print(name, 'has won the game. Congratulations!')
    else:
        print("It's a draw!")
    correct_input = False
    while not correct_input:
        print('1) Play again')
        print('0) Return to menu')
        ent = input('Enter number: ')
        if ent == '1':
            return True
        if ent == '0':
            return False
        clear()


def player_action(name, board, turn):
    board.draw_board()
    print(name + ', is your turn, playing as', X if turn else O)
    player_input(turn, board)


def pvp():
    keep_playing = True
    player_x_name = input('Player X name: ')
    player_o_name = input('Player O name: ')
    while keep_playing:
        print('    -- Game Starts --')
        game_end = const_game_end
        winner = const_winner
        player_x_turn = const_player_x_turn
        board = Board()

        while not game_end:
            if player_x_turn:
                player_action(player_x_name, board, player_x_turn)
                player_x_turn = False
            else:
                player_action(player_o_name, board, player_x_turn)
                player_x_turn = True

            if board.check_ending_state():
                game_end = True
            if board.check_win(X if not player_x_turn else O):
                game_end = True
                winner = True

        board.draw_board()
        if not player_x_turn:
            keep_playing = declare_winner(player_x_name, winner)
        else:
            keep_playing = declare_winner(player_o_name, winner)


def cpu_dumb():
    keep_playing = True
    player_x_name = input('Player X name: ')
    while keep_playing:
        print('    -- Game Starts --')
        game_end = const_game_end
        winner = const_winner
        player_x_turn = const_player_x_turn
        board = Board()

        dumb = DumbBot(board)
        player_o_name = dumb.name

        while not game_end:
            if player_x_turn:
                player_action(player_x_name, board, player_x_turn)
                player_x_turn = False
            else:
                dumb.dumb_action()
                player_x_turn = True

            if board.check_ending_state():
                game_end = True
            if board.check_win(X if not player_x_turn else O):
                game_end = True
                winner = True

        board.draw_board()
        if not player_x_turn:
            keep_playing = declare_winner(player_x_name, winner)
        else:
            keep_playing = declare_winner(player_o_name, winner)


def cpu_smart():
    keep_playing = True
    player_x_name = input('Player X name: ')
    while keep_playing:
        print('    -- Game Starts --')
        game_end = const_game_end
        winner = const_winner
        player_x_turn = const_player_x_turn
        board = Board()

        smart = SmartBot(board)
        player_o_name = smart.name

        while not game_end:
            if player_x_turn:
                player_action(player_x_name, board, player_x_turn)
                player_x_turn = False
            else:
                smart.smart_action()
                player_x_turn = True

            if board.check_ending_state():
                game_end = True
            if board.check_win(X if not player_x_turn else O):
                game_end = True
                winner = True

        board.draw_board()
        if not player_x_turn:
            keep_playing = declare_winner(player_x_name, winner)
        else:
            keep_playing = declare_winner(player_o_name, winner)


def cpu_dumb_dumb():
    keep_playing = True
    while keep_playing:
        print('    -- Game Starts --')
        game_end = const_game_end
        winner = const_winner
        player_x_turn = const_player_x_turn
        board = Board()

        dumb_x = DumbBot(board, 'DumbX', X)
        dumb_o = DumbBot(board, 'DumbO', O)
        player_x_name = dumb_x.name
        player_o_name = dumb_o.name

        while not game_end:
            sleep(1)
            if player_x_turn:
                dumb_x.dumb_action()
                player_x_turn = False
            else:
                dumb_o.dumb_action()
                player_x_turn = True
            board.draw_board()

            if board.check_ending_state():
                game_end = True
            if board.check_win(X if not player_x_turn else O):
                game_end = True
                winner = True

            board.draw_board()
            board.draw_board()
        if not player_x_turn:
            keep_playing = declare_winner(player_x_name, winner)
        else:
            keep_playing = declare_winner(player_o_name, winner)


def cpu_smart_smart():
    keep_playing = True
    while keep_playing:
        print('    -- Game Starts --')
        game_end = const_game_end
        winner = const_winner
        player_x_turn = const_player_x_turn
        board = Board()

        smart_x = SmartBot(board, 'SmartX', X)
        smart_o = SmartBot(board, 'SmartO', O)
        player_x_name = smart_x.name
        player_o_name = smart_o.name

        while not game_end:
            sleep(1)
            if player_x_turn:
                smart_x.smart_action()
                player_x_turn = False
            else:
                smart_o.smart_action()
                player_x_turn = True
            board.draw_board()

            if board.check_ending_state():
                game_end = True
            if board.check_win(X if not player_x_turn else O):
                game_end = True
                winner = True

            board.draw_board()
            board.draw_board()
        if not player_x_turn:
            keep_playing = declare_winner(player_x_name, winner)
        else:
            keep_playing = declare_winner(player_o_name, winner)


def cpu_smart_dumb():
    keep_playing = True
    while keep_playing:
        print('    -- Game Starts --')
        game_end = const_game_end
        winner = const_winner
        player_x_turn = const_player_x_turn
        board = Board()

        smart_x = SmartBot(board, 'SmartX', X)
        dumb_o = DumbBot(board, 'DumbO', O)
        player_x_name = smart_x.name
        player_o_name = dumb_o.name

        while not game_end:
            sleep(1)
            if player_x_turn:
                smart_x.smart_action()
                player_x_turn = False
            else:
                dumb_o.dumb_action()
                player_x_turn = True
            board.draw_board()
            if board.check_ending_state():
                game_end = True
            if board.check_win(X if not player_x_turn else O):
                game_end = True
                winner = True

            board.draw_board()
            board.draw_board()
        if not player_x_turn:
            keep_playing = declare_winner(player_x_name, winner)
        else:
            keep_playing = declare_winner(player_o_name, winner)


"""execution starts here"""
clear()
print('    -- Welcome --')
print('********************')
print()
print('Player X starts by default')
print()
print('********************')
print()
menu_loop = True
correct_input = False
while not correct_input and menu_loop:
    print('  Select game mode  ')
    print('--------------------')
    print('1) PvP')
    print('2) Player vs. CPU (DumbBot)')
    print('3) Player vs. CPU (SmartBot)')
    print('4) CPU vs. CPU (Dumb vs Dumb)')
    print('5) CPU vs. CPU (Smart vs Smart)')
    print('6) CPU vs. CPU (Smart vs Dumb)')
    print('0) Exit')
    print('')
    ent = input('Input number: ')
    if ent == '1':
        pvp()
    elif ent == '2':
        cpu_dumb()
    elif ent == '3':
        cpu_smart()
    elif ent == '4':
        cpu_dumb_dumb()
    elif ent == '5':
        cpu_smart_smart()
    elif ent == '6':
        cpu_smart_dumb()
    elif ent == '0':
        menu_loop = False
    clear()
print('See you next time')
