#!/usr/bin/python3

import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    for line in f:
        inputs.append(data_type(line[:-1]))

board = []
for i in range(1000):
    board.append([0] * 1000)

print()
print('PART ONE')
overlap = 0
# Line format
#1 @ 249,597: 20x15
lines = []
for line in inputs:
    ln, _, pos, dim = line.split()
    x, y = pos.split(',')
    x = int(x)
    y = int(y[:-1])
    w, h = map(int, dim.split('x'))
    lines.append((ln, x, y, w, h))
    for r in range(x, x+w):
        for c in range(y, y+h):
            # if slot is 0, no entry there yet - mark it but don't count it
            # if slot is 1, one entry there - this is the first overlap, count it
            # if slot is 2, two or more entries there - don't double count this overlap
            if board[r][c] == 1:
                overlap += 1
                board[r][c] = 2
            elif board[r][c] == 0:
                board[r][c] = 1
print(overlap)

print()
print('PART TWO')

for ln, x, y, w, h in lines:
    alone = True
    for r in range(x, x+w):
        for c in range(y, y+h):
            if board[r][c] != 1:
                alone = False
                break
        else:
            continue
        break
    if alone:
        print(ln[1:])
        break
