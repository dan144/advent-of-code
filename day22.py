#!/usr/bin/python3 -u

import json
import sys

from copy import copy

print('Running:',sys.argv[0])

testing = len(sys.argv) == 2 and sys.argv[1] == '-t'

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

depth = int(inputs[0].split()[1])
tx, ty = list(map(int, inputs[1].split()[1].split(',')))
maxx = int(tx * 5)  # determine a better way to detect the max
maxy = int(ty * 1)

print()
print('PART ONE')
ans = None

minm = None
cave = []
risk_level = 0
for y in range(maxy+1):
    cave.append([])
    for x in range(maxx+1):
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
        if x <= tx and y <= ty:
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

def move(spots):
    global mcosts
    n = []
    for spot in spots:
        if minm is not None and spot[3] >= minm:
            continue
        x, y, equipped, ocost, seen, changes = spot

        for dx, dy in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
            if x + dx < 0 or y + dy < 0 or x + dx > maxx or y + dy > maxy or (x + dx, y + dy) in seen:
                continue

            if cave[y+dy][x+dx] % 3 == ROCKY:
                next_set = {(WET, TORCH), (NARROW, CLIMBING)}
            elif cave[y+dy][x+dx] % 3 == WET:
                next_set = {(ROCKY, NEITHER), (NARROW, CLIMBING)}
            elif cave[y+dy][x+dx] % 3 == NARROW:
                next_set = {(ROCKY, NEITHER), (WET, TORCH)}

            for rtype, nequip in next_set:
                if cave[y][x] % 3 == rtype:  # the current region doesn't allow this equipment
                    continue
                if equipped == nequip:
                    cost = 1
                    changed = 0
                else:
                    cost = 8
                    changed = 1
                if minm is not None and ocost + cost >= minm:
                    continue
                if mcosts[nequip][y+dy][x+dx] is not None and ocost + cost >= mcosts[nequip][y+dy][x+dx]:
                    continue
                mcosts[nequip][y+dy][x+dx] = ocost + cost
                nseen = copy(seen)
                nseen.append((x+dx, y+dy))
                n.append((x+dx, y+dy, nequip, ocost + cost, nseen, changes + changed))
    return n


# make the program more efficient by keeping track of the lowest seen cost of x/y/equip combos
# mcosts is referenced by [equip][y][x]
mcosts = []
for e in range(3):
    mcosts.append([])
    for y in range(maxy+1):
        mcosts[-1].append([])
        for x in range(maxx+1):
            mcosts[-1][y].append(None)

ROCKY = 0   # torch, climbing
WET = 1     # climbing, neither
NARROW = 2  # torch, neither

TORCH = 0
CLIMBING = 1
NEITHER = 2

# x, y, equipped, cost, history, changes
spots = [(0, 0, TORCH, 0, [(0,0)], 0)]
left = []
spath = None
fchange = None
print('     Left  Minimum')
while spots or left:
    for spot in spots:
        if spot[0] == tx and spot[1] == ty:
            cost = spot[3]
            if spot[2] == TORCH:
                cost += 0
                changed = 0
            else:
                cost += 7
                changed = 1
            if minm is None or cost < minm:
                minm = cost
                spath = spot[4]
                fchange = spot[5] + changed
        else:
            if minm is None or spot[3] < minm:
                left.append(spot)
    left.sort(key=lambda x: x[3], reverse=True)
    spots = []
    for i in range(300):  # sending the whole spots list at once gets slow: chunk it
        if left:
            spots.append(left.pop())
    spots = move(spots)
    print(' {:8d} {:>8s}\r'.format(len(spots) + len(left), str(minm) if minm is not None else '?'), end='')

ans = minm
print()
print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
