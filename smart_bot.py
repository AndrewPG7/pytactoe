import random
from copy import deepcopy


class SmartBot:
    corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
    side = [(1, 0), (1, 2), (0, 1), (2, 1)]

    def __init__(self, board, name, symb):
        self.game_board = board
        self.name = name
        self.symb = symb

    def smart_action(self):
        if self.bot_win_move():
            return
        if self.player_win_move():
            return
        if self.corner_move():
            return
        if self.center_move():
            return
        if self.side_move():
            return

    def bot_win_move(self):
        for i in range(self.game_board.rows):
            for j in range(self.game_board.columns):
                c_board = deepcopy(self.game_board)
                if c_board.check_tile(i, j):
                    c_board.write_on_board(self.symb, i, j)
                    if c_board.check_win(self.symb):
                        self.game_board.write_on_board(self.symb, i, j)
                        return True

    def player_win_move(self):
        for i in range(self.game_board.rows):
            for j in range(self.game_board.columns):
                c_board = deepcopy(self.game_board)
                if c_board.check_tile(i, j):
                    if self.symb == 'O':
                        c_board.write_on_board('X', i, j)
                        if c_board.check_win('X'):
                            self.game_board.write_on_board(self.symb, i, j)
                            return True
                    else:
                        c_board.write_on_board('O', i, j)
                        if c_board.check_win('O'):
                            self.game_board.write_on_board(self.symb, i, j)
                            return True

    def corner_move(self):
        sample = random.sample(self.corner, 4)
        for i in sample:
            if self.game_board.check_tile(i[0], i[1]):
                self.game_board.write_on_board(self.symb, i[0], i[1])
                return True

    def center_move(self):
        if self.game_board.check_tile(1, 1):
            self.game_board.write_on_board(self.symb, 1, 1)
            return True

    def side_move(self):
        sample = random.sample(self.side, 4)
        for i in sample:
            if self.game_board.check_tile(i[0], i[1]):
                self.game_board.write_on_board(self.symb, i[0], i[1])
                return True
