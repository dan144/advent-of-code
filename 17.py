#!/usr/bin/env python3

import re
import sys

from computer import parse, run

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
print(mn, mx)

def run(board, r):
    n = {}
    for x in range(mn[0]-r, mx[0] + 1 + r):
        for y in range(mn[1]-r, mx[1] + 1 + r):
            for z in range(mn[2]-r, mx[2] + 1 + r):
                for w in range(mn[3]-r, mx[3] + 1 + r):
                    adj = 0
                    for dz in {-1, 0, 1}:
                        for dy in {-1, 0, 1}:
                            for dx in {-1, 0, 1}:
                                for dw in {-1, 0, 1}:
                                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                        continue
                                    nw, nz, ny, nx = w + dw, z + dz, y + dy, x + dx
                                    if (nx, ny, nz, nw) not in board:
                                        continue
                                    adj += board.get((nx, ny, nz, nw)) == '#'
                    # print(x, y, z, adj)
                    if board.get((x, y, z, w)) == '#':
                        if adj in {2, 3}:
                            n[x, y, z, w] = '#'
                    if board.get((x, y, z, w), '.') == '.':
                        if adj == 3:
                            n[x, y, z, w] = '#'
    return n

def disp(board):
    print(board)
    print(list(board.values()).count('#'))
disp(board)

for r in range(6):
    board = run(board, r+1)
    # disp(board)

p1 = list(board.values()).count('#')
print(f'Part 1: {p1}')


print(f'Part 2: {p2}')
