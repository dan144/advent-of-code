#!/usr/bin/env python3

import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

nodes = {}
with open(input_file) as f:
    for line in f:
        try:
            d = re.findall(r'\d+', line)
            x = int(d.pop(0))
            y = int(d.pop(0))
            # size, used, available, percent
            nodes[x, y] = list(map(int, d))
            if nodes[x, y][1] == 0:
                empty_node = x, y
        except IndexError:
            pass

for l1 in nodes.keys():
    for l2 in nodes.keys():
        nA = nodes[l1]
        nB = nodes[l2]
        if nA[1] != 0 and l1 != l2 and nA[1] <= nB[2]:
            p1 += 1

print(f'Part 1: {p1}')

def display(nodes):
    max_y = max({y for _, y in nodes.keys()})
    for y in range(max_y+1):
        for (mx, my), data in nodes.items():
            if my != y:
                continue
            print(f'{data[1]!s:>3}/{data[0]!s:>3}', end=' ')
        print()

if test:
    display(nodes)

# 1. move blocks to empty slot left of goal data (28 steps for my input)
# 2. move goal into empty slot
# 3. cycle blocks around goal data and move goal toward 0,0 - 5 steps each

max_x = max({x if y == 0 else 0 for x, y in nodes.keys()}) - 1

# determine legal distance from empty to target node
grid = {(x, y): data[0] < 100 for (x, y), data in nodes.items()}
first_dist = utils.find_dist(grid, 0, {empty_node}, (max_x, 0))

p2 = first_dist + 1 + 5 * max_x
print(f'Part 2: {p2}')
