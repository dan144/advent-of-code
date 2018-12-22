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

depth = int(inputs[0].split()[1])
tx, ty = list(map(int, inputs[1].split()[1].split(',')))

cave = []
risk_level = 0
for y in range(ty+1):
    cave.append([])
    for x in range(tx+1):
        if x == 0 and y == 0:
            geologic = 0
        elif x == tx and y == ty:
            geologic = 0
        elif y == 0:
            geologic = x * 16807
        elif x == 0:
            geologic = y * 48271
        else:
            geologic = cave[y][x-1] * cave[y-1][x]
        erosion = (geologic + depth) % 20183
        cave[y].append(erosion)
        risk_level += (erosion % 3)

ans = risk_level
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
