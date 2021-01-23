#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

dirs = []
with open(input_file) as f:
    dirs = f.readline().rstrip().split(', ')

x, y = 0, 0
direction = 0
visited = set()
for d in dirs:
    turn, dist = d[0], int(d[1:])
    direction += 1 if turn == 'R' else -1
    direction %= 4
    for i in range(dist):
        if direction % 2 == 0: # N/S
            y += 1 if direction == 0 else -1
        else:
            x += 1 if direction == 1 else -1
        if (x, y) in visited and not p2:
            p2 = utils.manh((x, y))
        visited.add((x, y))

p1 = utils.manh((x, y))
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
