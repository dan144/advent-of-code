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

def nest(level):
    global parsed, x
    global inp
    p = [[]]
    #print(p[0])
    while inp:
        c = inp.pop(0)
        parsed += 1
        #print(level, c)
        if c in 'NEWS':
            p[-1].append(c)
        elif c == '(':
            x[0] += 1
            if False and level < 3:
                input()
            p[-1].append([nest(level+1)])
            #h1 = nest(level+1)
            #h2 = nest(level+1)
            #p.append([h1, h2])
        elif c == ')':
            x[1] += 1
            if False and level < 3:
                input()
            break
            #return paths
        elif c == '|':
            x[2] += 1
            p.append([])
            #if level < 3:
            #    input()
            #break
            #return paths
        else:
            print('AGH')
    #print('NAW')
    #input()
    return p


parsed = 0
inp = list(inputs[0][1:-1])
x = [0,0,0]
#for c in inp:
#    if c == '(':
#        x[0] += 1
#    elif c == ')':
#        x[1] += 1
#    elif c == '|':
#        x[2] += 1
todo = len(inp)
paths = nest(0)
#print(paths)
print(x)
#print(''.join(paths))
print(todo, parsed, len(inp))

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


def parse(paths, x, y, level):
    global board, pos
    global levels
    ax = x
    ay = y
    ox = None
    oy = None
    #d = [0, 0]
    for v in paths:
        #print(x, y, v)
        if v == 'N':
            board[y][x][N] = True
            if y == 0:
                board.insert(0, [])
                pos[1] += 1
                #d[1] += 1
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
                #d[0] += 1
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
            ax = x
            ay = y
            aposx = pos[0]
            aposy = pos[1]
            for p in v:
                if type(p) is list:
                    ox = x
                    oy = y
                    oposx = pos[0]
                    oposy = pos[1]
                #print('OK', p, ox, oy)
                x, y = parse(p, x, y, level + 1)
                if type(p) is list:
                    x = ox + pos[0] - oposx
                    y = oy + pos[1] - oposy
                #print('DONE', x, y, ox, oy)
            #print('LEVELDONE')
            x = ax + pos[0] - aposx
            y = ay + pos[1] - aposy

        #draw_board()
        #print(pos, level, x, y)
        #input()
    #return d
    return x, y

pos = [0, 0]
parse(paths, 0, 0, 0)

dirs = [[0, W, 0],
        [N, 0, S],
        [0, E, 0]]

def move_from(reachable, distance):
    global seen
    n = []
    for spot in reachable:
        x, y = spot
        for dx, dy in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
            if y + dy in range(len(board)) and x + dx in range(len(board[0])):
                p = (x + dx, y + dy)
                if p not in seen and board[y][x][dirs[dx+1][dy+1]]:
                    seen.add(p)
                    n.append(p)
    print(n)
    return n if n else distance
    return move_from(n, distance+1) if n else distance

draw_board()

reachable = [pos]
seen = {(pos[0], pos[1])}
try:
    i = 0
    ans = -1
    while type(reachable) is list:
        i += 1
        reachable = move_from(reachable, 0)
        ans += 1
except:
    raise
    sys.exit(1)

print(pos)
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')
ans = None



print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
