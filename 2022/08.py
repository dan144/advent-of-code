#!/usr/bin/env python3

import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# find_cheapest(grid, (y,x) start, (y,x) end) - grid of ints, finds cheapest path from start to end, returns cost dist
# transpose_grid(grid) - swap key values from (x, y) to (y, x) and back
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime
# adjs - set of dx,dy values for LRUD adjacencies
# diags - set of dx,dy values for diagonals
# all_dirs set of dx,dy values for all 8 surrounding values

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    grid = utils.load_grid(f, str) # 2D grid of X type

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
for (x, y), height in grid.items():
    blocked = 0
    score = 1
    i = 0
    for nx in range(x - 1, min_x - 1, -1):
        i += 1
        if grid.get((nx, y), 0) >= height:
            blocked += 1
            break
    score *= i
    i = 0
    for nx in range(x + 1, max_x + 1):
        i += 1
        if grid.get((nx, y), 0) >= height:
            blocked += 1
            break
    score *= i
    i = 0
    for ny in range(y - 1, min_y - 1, -1):
        i += 1
        if grid.get((x, ny), 0) >= height:
            blocked += 1
            break
    score *= i
    i = 0
    for ny in range(y + 1, max_y + 1):
        i += 1
        if grid.get((x, ny), 0) >= height:
            blocked += 1
            break
    score *= i
    p2 = max(p2, score)
    if blocked < 4:
        p1 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
