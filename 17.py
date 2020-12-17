#!/usr/bin/env python3

import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

board = {}
y = 0
with open(input_file) as f:
    for line in f:
        for x, c in enumerate(line[:-1]):
            board[x, y, 0, 0] = c
        y += 1

mn = [0, 0, 0, 0]
mx = [x, y-1, 0, 0]
board2 = copy(board)

def run(board, r, run_w):
    n = {}
    w_range = range(mn[3]-r, mx[3] + 1 + r) if run_w else {0}
    dw_range = {-1, 0, 1} if run_w else {0}

    for x in range(mn[0]-r, mx[0] + 1 + r):
        for y in range(mn[1]-r, mx[1] + 1 + r):
            for z in range(mn[2]-r, mx[2] + 1 + r):
                for w in w_range:
                    adj = 0
                    for dz in {-1, 0, 1}:
                        for dy in {-1, 0, 1}:
                            for dx in {-1, 0, 1}:
                                for dw in dw_range:
                                    if not any((dx, dy, dz, dw)):
                                        continue
                                    nw, nz, ny, nx = w + dw, z + dz, y + dy, x + dx
                                    if (nx, ny, nz, nw) not in board:
                                        continue
                                    adj += board.get((nx, ny, nz, nw)) == '#'
                    if board.get((x, y, z, w)) == '#':
                        if adj in {2, 3}:
                            n[x, y, z, w] = '#'
                    if board.get((x, y, z, w), '.') == '.':
                        if adj == 3:
                            n[x, y, z, w] = '#'
    return n

for r in range(6):
    board = run(board, r+1, False)

p1 = list(board.values()).count('#')
print(f'Part 1: {p1}')

for r in range(6):
    board2 = run(board2, r+1, True)

p2 = list(board2.values()).count('#')
print(f'Part 2: {p2}')
