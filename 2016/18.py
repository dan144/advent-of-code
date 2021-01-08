#!/usr/bin/env python3

import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    row = list(f.readline().rstrip())

o_grid = {}
y = 0
for x, c in enumerate(row):
    o_grid[x, y] = c == '^'

def run(grid, n_row):
    for y in range(1, n_row):
        for x in range(len(row)):
            l = grid.get((x - 1, y - 1), False)
            c = grid.get((x, y - 1), False)
            r = grid.get((x + 1, y - 1), False)

            m = any((
                l and c and not r,
                c and r and not l,
                l and not r and not c,
                r and not l and not c,
            ))

            grid[x, y] = m


grid = copy(o_grid)
run(grid, 10 if test else 40)
p1 = len(grid.values()) - sum(grid.values())
print(f'Part 1: {p1}')

if test:
    sys.exit(0)

grid = copy(o_grid)
run(grid, 10 if test else 400000)
p2 = len(grid.values()) - sum(grid.values())
print(f'Part 2: {p2}')
