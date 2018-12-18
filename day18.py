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

if testing:
    for line in board:
        print(''.join(line))

vals = []
wooded = 0
lumber = 0
for t in range(1, 1000):  # does not need to be all of 1000000000, just enough to force a cycle
    wooded = 0
    lumber = 0

    n = []
    for y in range(len(board)):
        n.append([])
        for x in range(len(board[0])):
            w = 0
            l = 0
            for j in range(max(0, y-1), min(len(board)-1, y+1)+1):
                for i in range(max(0, x-1), min(len(board[0])-1, x+1)+1):
                    if j == y and i == x:
                        continue
                    if board[j][i] == '|':
                        w += 1
                    elif board[j][i] == '#':
                        l += 1

            if board[y][x] == '.' and w >= 3:
                n[-1].append('|')
                wooded += 1
            elif board[y][x] == '|' and l >= 3:
                n[-1].append('#')
                lumber += 1
            elif board[y][x] == '#' and (l == 0 or w == 0):
                n[-1].append('.')
            else:
                n[-1].append(board[y][x])
                wooded += 1 if board[y][x] == '|' else 0
                lumber += 1 if board[y][x] == '#' else 0
    board = n

    vals.append(wooded * lumber)
    if t == 10:
        ans = vals[-1]
        print()
        print('PART ONE')
        print(t, ans)
        if testing:
            if part_one == ans:
                print('PART ONE CORRECT')
            else:
                print('PART ONE FAILED')

    if t > 0 and t % 50 == 0:
        print('Computed', t, 'minutes')

cycle = 1
while vals[-1] != vals[-1-cycle]:
    cycle += 1
first = 1000000000 % cycle - 1
t_ans = (int(len(vals)/cycle) - 1) * cycle + first
ans = vals[t_ans]

print()
print('PART TWO')
print('Values repeat every:', cycle)
print('1000000000', ans)

if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
