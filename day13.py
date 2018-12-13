#!/usr/bin/python3

import json
import sys

print('Running:',sys.argv[0])

testing = len(sys.argv) == 2

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)

if testing:
    print('TESTING')
    input_file = 'test' + input_file

print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    if testing:
        test_vals = json.loads(f.readline())
        part_one = test_vals['part_one']
        part_two = test_vals['part_two']
    for line in f:
        inputs.append(data_type(line[:-1]))
if testing:
    print(inputs)

board = []
carts = []
tick = 0
ncarts = 0

y = 0
for line in inputs:
    board.append(list(line))
    carts.append([None] * len(line))
    x = 0
    for c in line:
        if c in '<>^v':
            ncarts += 1
            carts[y][x] = [c, 0, tick]
            if c in '<>':
                board[y][x] = '-'
            else:
                board[y][x] = '|'
        x += 1
    y += 1

my = len(board)
mx = len(board[0])
crash = None
ans = None

print('Total carts:', ncarts)

print()
print('PART ONE')

while ncarts > 1:
    for y in range(my):
        for x in range(mx):
            if carts[y][x] is None or carts[y][x][2] > tick:
                continue
            m = carts[y][x][0] + board[y][x]
            if m in {'<-', '^\\', 'v/'}:
                ny, nx, c, d = y, x-1, '<', carts[y][x][1]
            elif m in {'>-', '^/', 'v\\'}:
                ny, nx, c, d = y, x+1, '>', carts[y][x][1]
            elif m in {'v|', '</', '>\\'}:
                ny, nx, c, d = y+1, x, 'v', carts[y][x][1]
            elif m in {'^|', '<\\', '>/'}:
                ny, nx, c, d = y-1, x, '^', carts[y][x][1]
            elif board[y][x] == '+':
                if carts[y][x][1] == 0:  # left
                    if carts[y][x][0] == '<':
                        ny, nx, c, d = y+1, x, 'v', 1
                    elif carts[y][x][0] == 'v':
                        ny, nx, c, d = y, x+1, '>', 1
                    elif carts[y][x][0] == '>':
                        ny, nx, c, d = y-1, x, '^', 1
                    elif carts[y][x][0] == '^':
                        ny, nx, c, d = y, x-1, '<', 1
                if carts[y][x][1] == 1:  # straight
                    if carts[y][x][0] == '<':
                        ny, nx, c, d = y, x-1, '<', 2
                    elif carts[y][x][0] == 'v':
                        ny, nx, c, d = y+1, x, 'v', 2
                    elif carts[y][x][0] == '>':
                        ny, nx, c, d = y, x+1, '>', 2
                    elif carts[y][x][0] == '^':
                        ny, nx, c, d = y-1, x, '^', 2
                if carts[y][x][1] == 2:  # right
                    if carts[y][x][0] == '<':
                        ny, nx, c, d = y-1, x, '^', 0
                    elif carts[y][x][0] == 'v':
                        ny, nx, c, d = y, x-1, '<', 0
                    elif carts[y][x][0] == '>':
                        ny, nx, c, d = y+1, x, 'v', 0
                    elif carts[y][x][0] == '^':
                        ny, nx, c, d = y, x+1, '>', 0
            if carts[ny][nx] is not None:
                if crash is None:
                    crash = ','.join((str(nx), str(ny)))
                    print(crash)
                carts[y][x] = None
                carts[ny][nx] = None
                ncarts -= 2
                print('Remaining carts:', ncarts)
            else:
                carts[ny][nx] = [c, d, tick+1]
                carts[y][x] = None
    tick += 1

ans = crash
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')
ans = None

for y in range(len(carts)):
    for x in range(len(carts[0])):
        if carts[y][x]:
            ans = ','.join((str(x), str(y)))
            break

print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
