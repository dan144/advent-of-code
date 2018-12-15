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

HP = 200
AP = 3
class Goblin():
    def __init__(self, x, y):
        self.hp = HP
        self.x = x
        self.y = y
    def __str__(self):
        return 'G'
class Elf():
    def __init__(self, x, y):
        self.hp = HP
        self.x = x
        self.y = y
    def __str__(self):
        return 'E'

goblins = []
elves = []
board = []
for y in range(len(inputs)):
    line = inputs[y]
    board.append([])
    for x in range(len(line)):
        c = line[x]
        if c in '.#':
            board[-1].append(c)
        elif c == 'G':
            g = Goblin(x, y)
            board[-1].append(g)
            goblins.append(g)
        elif c == 'E':
            e = Elf(x, y)
            board[-1].append(e)
            elves.append(e)

for line in board:
    print(''.join(map(str, line)))

print(elves)
print(goblins)
while len(elves) and len(goblins):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if type(board[y][x]) in {Goblin, Elf}:
                print(board[y][x])
                target_locs = []
                target_array = goblins if type(board[y][x]) == Elf else elves
                for target in target_array:
                    tx = target.x
                    ty = target.y
                    for xoff, yoff in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
                        if board[ty+yoff][tx+xoff] == '.':
                            target_locs.append((ty+yoff, tx+xoff))
                            board[ty+yoff][tx+xoff] = '?'
                break
        else:
            continue
        break
    break

for line in board:
    print(''.join(map(str, line)))


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
