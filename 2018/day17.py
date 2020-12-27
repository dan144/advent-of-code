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
ans = 0

points = set()
minx = None
maxx = None
miny = None
maxy = None
for line in inputs:
    ls = line.split(', ')
    if line.startswith('x'):
        x0 = int(ls[0].split('=')[1])
        x1 = x0
        y0, y1 = list(map(int, ls[1].split('=')[1].split('..')))
    else:
        y0 = int(ls[0].split('=')[1])
        y1 = y0
        x0, x1 = list(map(int, ls[1].split('=')[1].split('..')))

    if minx is None or x0 < minx:
        minx = x0
    if maxx is None or x1 > maxx:
        maxx = x1
    if miny is None or y0 < miny:
        miny = y0
    if maxy is None or y1 > maxy:
        maxy = y1
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            points.add((x, y))

sources = [(501 - minx, 0)]

board = []
p1 = 0
for y in range(miny, maxy+1):
    board.append(['.'])
    for x in range(minx, maxx + 1):
        board[-1].append('#' if (x, y) in points else '.')
        if (x, y) in points:
            p1 += 1
    board[-1].append('.')


def add_water(source, y=None):
    global minx, board

    ns = []
    sx = source[0]

    if y is None:
        y = source[1]
        if board[y][sx] == '.':
            board[y][sx] = '|'
        while board[y][sx] not in '~#' and y < len(board) - 1:
            if board[y+1][sx] == '.':
                board[y+1][sx] = '|'
            y += 1
        if y == len(board) - 1 and board[y][sx] != '#':
            return False
        y -= 1

    mx = None
    xx = None
    for dx in range(len(board[y])):
        if board[y][dx] == '#':
            if dx <= sx:
                mx = dx
            elif xx is None and dx >= sx:
                xx = dx
                break

    if mx is not None and xx is not None:
        below = board[y+1][mx:xx+1]
        if all([v in '~#' for v in below]):
            for x in range(mx+1, xx):
                board[y][x] = '~'
            return add_water(source, y-1)

    for x in range(sx-1, mx if mx is not None else -1, -1):
        if board[y][x] == '.':
            board[y][x] = '|'
        if board[y+1][x] == '.':
            ns.append((x, y))
            break
        elif board[y+1][x] == '|':
            break
    for x in range(sx, xx if xx is not None else len(board[y+1])):
        if board[y][x] == '.':
            board[y][x] = '|'
        if board[y+1][x] == '.':
            ns.append((x, y))
            break
        elif board[y+1][x] == '|':
            break

    return ns if ns else False


old = set()
while sources:
    r = add_water(sources[0])
    sources.extend([s for s in r if s not in old and s not in sources] if r else [])
    old.add(sources.pop(0))

    if testing:
        for line in board:
            print(''.join(line))
        print()

ans2 = 0
for line in board:
    for c in line:
        if c in '~':
            ans2 += 1
        if c == '|':
            ans += 1

ans += ans2
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')
ans = ans2

print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
