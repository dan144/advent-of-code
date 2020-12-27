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
data_type = int
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

board = []
for b in range(300):
    board.append([0] * 300)

gridSI = inputs[0]
for x in range(300):
    for y in range(300):
        rackId = x + 10
        powerLevel = rackId * y
        powerLevel += gridSI
        powerLevel *= rackId
        powerLevel = int(powerLevel / 100) % 10
        powerLevel -= 5
        board[y][x] = powerLevel

def run(size, vals):
    for x in range(300 - size):
        for y in range(300 - size):
            s = 0
            for i in range(size):
                s += sum(board[y+i][x:x+size])
            if vals.m is None or s > vals.m:
                vals.m = s
                vals.mx = x
                vals.my = y
                vals.s = size

class S():
    def __init__(self):
        self.m = None
        self.mx = 1
        self.my = 1
        self.s = 1

vals = S()
run(3, vals)

ans = ','.join((str(vals.mx), str(vals.my)))
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')


print()
print('PART TWO')
ans = None

vals = S()
#for size in range(3, 4):
for size in range(1, 301):
    print(size)
    run(size, vals)
ans = ','.join((str(vals.mx), str(vals.my), str(vals.s)))

print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
