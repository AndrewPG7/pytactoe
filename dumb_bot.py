import random

class DumbBot:

    def __init__(self, board, name, symb):
        self.game_board = board
        self.name = name
        self.symb = symb

    def dumb_action(self):
        bullseye = False
        while not bullseye:
            i = random.randint(0, 2)
            j = random.randint(0, 2)

            if self.game_board.board[i][j] == '-':
                self.game_board.write_on_board(self.symb, i, j)
                bullseye = True
