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

print()
print('PART ONE')
ans = None

def nest():
    global inp
    p = [[]]
    while inp:
        c = inp.pop(0)
        if c in 'NEWS':
            p[-1].append(c)
        elif c == '(':
            p[-1].append([nest()])
        elif c == ')':
            break
        elif c == '|':
            p.append([])
    return p


inp = list(inputs[0][1:-1])
paths = nest()

board = [[[False, False, False, False]]]
N = 0
E = 1
W = 2
S = 3

def draw_board():
    global board
    print()
    for line in board:
        for room in line:
            v = ['T' if x else 'F' for x in room]
            print(''.join(v), end=' ')
        print()
    print()


def parse(paths, x, y):
    global board, pos
    ax = x
    ay = y
    ox = None
    oy = None
    for v in paths:
        # if v is a letter: set x/y's door in that direction open,
        # check if moving that way is possible (if not extend the board),
        # set the new position's return door to open, modify x/y appropriately
        #
        # if the board changes size, your original position must change, as
        # well as x/y potentially not simply incrementing/decrementing
        if v == 'N':
            board[y][x][N] = True
            if y == 0:
                board.insert(0, [])
                pos[1] += 1
                for dx in range(len(board[1])):
                    board[0].append([False] * 4)
            else:
                y -= 1
            board[y][x][S] = True
        elif v == 'E':
            board[y][x][E] = True
            if x + 1 == len(board[0]):
                for dy in range(len(board)):
                    board[dy].append([False] * 4)
            x += 1
            board[y][x][W] = True
        elif v == 'W':
            board[y][x][W] = True
            if x == 0:
                pos[0] += 1
                for dy in range(len(board)):
                    board[dy].insert(0, [False] * 4)
            else:
                x -= 1
            board[y][x][E] = True
        elif v == 'S':
            board[y][x][S] = True
            if y + 1 == len(board):
                board.append([])
                for dx in range(len(board[0])):
                    board[-1].append([False] * 4)
            y += 1
            board[y][x][N] = True
        else:
            # after execution of all subpieces of thel ist, x/y should be restored
            # to their original values. In addition, any change in pos (your position)
            # must be considered, as it indicates that the board has grown N/W and
            # x/y must change accordingly
            aposx = pos[0]
            aposy = pos[1]
            dx = x
            dy = y
            for p in v:
                # if p is a list, then it's a split; x/y should be reset when it's done
                if type(p) is list:
                    ox = dx
                    oy = dy
                    oposx = pos[0]
                    oposy = pos[1]
                dx, dy = parse(p, dx, dy)
                if type(p) is list:
                    dx = ox + pos[0] - oposx
                    dy = oy + pos[1] - oposy
            x += pos[0] - aposx
            y += pos[1] - aposy

    return x, y

pos = [0, 0]
parse(paths, 0, 0)

dirs = [[0, W, 0],
        [N, 0, S],
        [0, E, 0]]


def move_from(reachable):
    global seen
    n = []
    for spot in reachable:
        x, y = spot
        for dx, dy in {(-1, 0), (0, -1), (0, 1), (1, 0)}:  # each cardinal direction
            # check if on the board
            if y + dy in range(len(board)) and x + dx in range(len(board[0])):
                p = (x + dx, y + dy)
                # check not seen and there's a
                if p not in seen and board[y][x][dirs[dx+1][dy+1]]:
                    # it has now been seen and is reachable in the next round
                    seen.add(p)
                    n.append(p)
    return n

if testing:
    draw_board()

reachable = [pos]
seen = {(pos[0], pos[1])}

dist = 0
beyond_1k = 0
while reachable:
    reachable = move_from(reachable)
    dist += 1
    if dist >= 1000:
        beyond_1k += len(reachable)

ans = dist - 1
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')

ans = beyond_1k
print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
