from string import ascii_uppercase
import math


class Board:
    def __init__(self, sudokuString):
        self.sudokuString = sudokuString

    def sudoku_board(self):
        n = int(pow(len(self.sudokuString), 0.5))  # length or breadth of board
        rowList = ascii_uppercase[:n]
        index = 0
        Board = {}  # Board = {A1: Cell, A2: cell}...  Dictionary
        domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        value = 0
        for row in rowList:  # cell = [value, domain]
            for col in range(1, n + 1):
                key = row + str(col)

                if self.sudokuString[index] != '0':
                    value = int(self.sudokuString[index])
                    domain = {value}
                Board[key] = domain
                index += 1
        return Board

    def display(self):
        n = len(self.sudokuString)
        nside = int(math.sqrt(n))
        for i in range(0, n, nside):
            nl = self.sudokuString[i:i + nside]
            print([int(s) for s in nl])
