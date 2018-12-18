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
for line in inputs:
    board.append(list(line))

for line in board:
    print(''.join(line))
for t in range(1, 1000000001):
    n = []
    for y in range(len(board)):
        n.append([])
        for x in range(len(board[0])):
            minx = max(0, x-1)
            maxx = min(len(board[0])-1, x+1)
            miny = max(0, y-1)
            maxy = min(len(board)-1, y+1)

            wooded = 0
            lumber = 0
            o = 0
            for j in range(miny, maxy+1):
                for i in range(minx, maxx+1):
                    if j == y and i == x:
                        continue
                    if board[j][i] == '.':
                        o +=1
                    elif board[j][i] == '|':
                        wooded += 1
                    elif board[j][i] == '#':
                        lumber += 1

            if board[y][x] == '.' and wooded >= 3:
                n[-1].append('|')
            elif board[y][x] == '|' and lumber >= 3:
                n[-1].append('#')
            elif board[y][x] == '#' and (lumber == 0 or wooded == 0):
                n[-1].append('.')
            else:
                n[-1].append(board[y][x])
    board = n

    if t == 10:
        wooded = 0
        lumber = 0
        for line in board:
            for c in line:
                if c == '|':
                    wooded += 1
                elif c == '#':
                    lumber += 1
        
        ans = wooded * lumber

        print()
        print('PART ONE')
        print(t, ans)
        if testing:
            if part_one == ans:
                print('PART ONE CORRECT')
            else:
                print('PART ONE FAILED')

    if (t-20) % 28 == 0: # This is hacky, improve this detection
        # basically every 28 iterations it repeats, and 1000000000 % 28 == 20, so offset it by that
        wooded = 0
        lumber = 0
        for line in board:
            for c in line:
                if c == '|':
                    wooded += 1
                elif c == '#':
                    lumber += 1
        
        ans = wooded * lumber
        print(t, ans)

        print()
        print('PART TWO')
        
        if testing:
            if part_two == ans:
                print('PART TWO CORRECT')
            else:
                print('PART TWO FAILED')
