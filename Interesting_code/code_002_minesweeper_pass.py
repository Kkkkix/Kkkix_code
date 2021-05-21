# -*- coding: utf-8 -*-
# This code is a minesweeper solver
# Author: Kkkkix
# Last Modified: 22/05/20
from win32 import win32gui



class Solver(object):
    def __init__(self, spaces):
        self.spaces = frozenset(spaces)
        self.solved_spaces = dict()
        self.information = set()
        self.informations_for_space = collections.defaultdict(set)
        self.spaces_to_add = []
        self.informations_to_add = []





def minesweeper_solver(width,height,mine_num):
    spaces = set((x, y) for x in range(width) for y in range(height))
    solver = Solver(spaces)


    # Find the window of minesweeper
    title_name = "Minesweeper Clone (32 bit)"







if __name__ == '__main__':
    #   Intermediate (width=16, height=16,mine_num=40)
    minesweeper_solver(width=16, height=16, mine_num=40)
