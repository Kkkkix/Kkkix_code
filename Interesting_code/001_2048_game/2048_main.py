# -*- coding:utf-8 -*-
import random
import numpy as np

"""
A small game : 2048

Kkkix
Modified date: 2022-01-05

"""


class GameBoard(object):

    def __init__(self):
        self.score = 0                      # initialize score
        self.main_board = np.zeros((4,4))   # initialize a game board, a 4*4 matrix
        self.game_over_flag = False
        self.init_game()

    def init_game(self):
        # Initialize the game
        n = random.sample(range(16),2)      # randomly select two position, change the number to 2
        self.main_board[n[0] // 4, n[0] % 4] = 2
        self.main_board[n[1] // 4][n[1] % 4] = 2

    def show(self):
        # Print the game board and score
        for y in range(4):
            for x in range(4):
                print(f"  {self.main_board[y][x]:4}  ", end='\t')
            print()
        print(f"Score is: {self.score}")

    def change_board_direction(self, direction):
        # Change the direction of the matrix in the board
        if direction == 'left':
            pass
        elif direction == 'right':
            for i in range(4):
                self.main_board[i] = self.main_board[i][::-1]
        elif direction == 'up':
            self.main_board = self.main_board.T
        elif direction == 'down':
            self.main_board = self.main_board.T
            for i in range(4):
                self.main_board[i] = self.main_board[i][::-1]
            self.main_board = self.main_board[[3, 2, 1, 0]]
        return self.main_board

    def move_num(self, direction):
        # Move non-zero numbers to the far left of the matrix
        # According to the command direction, invert or transpose matrix before move
        self.change_board_direction(direction)
        for i in range(4):
            c_line = self.main_board[i]         # current line
            temp_line = c_line[np.nonzero(c_line)]
            self.main_board[i] = np.append(temp_line, np.zeros(4-temp_line.size))
        self.change_board_direction(direction)

    def comb_adja_same_num(self, direction):
        # Combine adjacent same numbers in the operation direction
        # Change the direction of matrix first,
        # then do the combination command in the left direction
        # addscore is the score obtained in this command
        addscore = 0
        self.change_board_direction(direction)
        for i in range(4):
            for j in range(3):
                if self.main_board[i][j] != 0 and self.main_board[i][j] == self.main_board[i][j + 1]:
                    self.main_board[i][j] *= 2
                    self.main_board[i][j + 1] = 0
                    addscore += self.main_board[i][j]
        self.move_num("left")
        self.change_board_direction(direction)
        return addscore

    def operation(self):
        # Input the command and operate the board
        next_move = input("Please input the next operation: w(up) a(left) s(down) d(right)")
        if next_move == 'a':
            direction = 'left'
        elif next_move == 'd':
            direction = 'right'
        elif next_move == 's':
            direction = 'down'
        elif next_move == 'w':
            direction = 'up'

        temp_board_before = self.main_board.copy()
        self.move_num(direction)
        addscore = self.comb_adja_same_num(direction)
        self.score += addscore
        temp_board_after = self.main_board.copy()

        if not (temp_board_after == temp_board_before).all():
            self.rand_generator()
        else:
            print("The operation just now has no effect")

    def rand_generator(self):
        # Randomly select a empty position to generate a number 2 or 4
        posi = np.nonzero(self.main_board == 0)
        rand_num = random.sample(range(len(posi[0])), 1)
        self.main_board[posi[0][rand_num], posi[1][rand_num]] = 2

    def run_game(self):
        print("Game start")
        while not self.game_over_flag:
            print("Game running......")
            self.show()
            self.operation()


if __name__ == "__main__":
    Game1 = GameBoard()
    Game1.run_game()










