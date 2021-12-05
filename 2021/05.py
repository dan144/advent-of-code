#!/usr/bin/env python3

import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges: min_x, min_y, max_x, max_y
# display_grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    inp = utils.load_split_lines(f) # asdf asdf asdf ...

# Part 1
grid = {}
for line in inp:
    x1, y1 = map(int, line[0].split(','))
    x2, y2 = map(int, line[2].split(','))
    if x1 == x2:
        ymn, ymx = sorted([y1, y2])
        for y in range(ymn, ymx+1):
            v = grid.get((x1, y), 0)
            grid[x1, y] = v + 1
    elif y1 == y2:
        xmn, xmx = sorted([x1, x2])
        for x in range(xmn, xmx+1):
            v = grid.get((x, y1), 0)
            grid[x, y1] = v + 1
    else:
        xmn, xmx = sorted([x1, x2])
        ymn, ymx = sorted([y1, y2])
        d = xmx - xmn
        mul = 1 if (y1 > y2) == (x1 > x2) else -1
        for i in range(d+1):
            if mul == 1:
                xy = (xmn + i, ymn + i)
            else:
                xy = (xmn + i, ymx - i)
            v = grid.get(xy, 0)
            grid[xy] = v + 1

if test:
    utils.display_grid(grid)
for v in grid.values():
    if v > 1:
        p1 += 1
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
