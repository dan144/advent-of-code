#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.rstrip())

grid = {}
mx, my = (7, 3) if test else (50, 6)
for y in range(my):
    for x in range(mx):
        grid[x, y] = False

def show(grid):
    for y in range(my):
        for x in range(mx):
            print('.#'[grid[x, y]], end='')
        print()

for line in inp:
    new = {}
    if line.startswith('rect'):
        x, y = map(int, line.split()[1].split('x'))
        for sx in range(x):
            for sy in range(y):
                grid[sx, sy] = True
    elif line.startswith('rotate row'):
        y, dx = map(int, re.findall(r'\d+', line))
        for x in range(mx):
            new[(x + dx) % mx, y] = grid[x, y]
    elif line.startswith('rotate column'):
        x, dy = map(int, re.findall(r'\d+', line))
        for y in range(my):
            new[x, (y + dy) % my] = grid[x, y]

    grid.update(new)

p1 = sum(grid.values())
print(f'Part 1: {p1}')

show(grid)
