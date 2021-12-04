#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    inp = utils.load_split_lines(f) # asdf asdf asdf ...

# Part 1
nums = []
boards = None

board = []
for line in inp:
    if not line:
        if boards is None:
            boards = []
        else:
            boards.append(board)
        board = []
    elif not nums:
        nums = inp[0][0].split(',')
    else:
        board.append(line)
boards.append(board)

def wins(board):
    for x in range(5):
        for y in range(5):
            if isinstance(board[x][y], int):
                continue
            break
        else:
            return True

    for y in range(5):
        for x in range(5):
            if isinstance(board[x][y], int):
                continue
            break
        else:
            return True

    return False

def score(board, num):
    sub = 0
    for line in board:
        for lnum in line:
            if isinstance(lnum, str):
                sub += int(lnum)
    return sub * int(num)

winner = None
winners = set()
for num in nums:
    for i, board in enumerate(boards):
        for line in board:
            if num in line:
                x = line.index(num)
                assert x != -1
                line[x] = int(num)
        if wins(board):
            if winner is None:
                winner = i
                p1 = score(board, num)
            winners.add(i)
            if len(winners) == len(boards):
                if p2 == 0:
                    p2 = score(board, num)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
