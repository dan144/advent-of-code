#!/usr/bin/env python3

import math
import sys

import utils
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    grid = utils.load_grid(f, str) # 2D grid of X type

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
for (x, y), height in grid.items():
    blocked = 0
    score = [0, 0, 0, 0]
    for nx in range(x - 1, min_x - 1, -1):
        score[0] += 1
        if grid.get((nx, y), 0) >= height:
            blocked += 1
            break
    for nx in range(x + 1, max_x + 1):
        score[1] += 1
        if grid.get((nx, y), 0) >= height:
            blocked += 1
            break
    for ny in range(y - 1, min_y - 1, -1):
        score[2] += 1
        if grid.get((x, ny), 0) >= height:
            blocked += 1
            break
    for ny in range(y + 1, max_y + 1):
        score[3] += 1
        if grid.get((x, ny), 0) >= height:
            blocked += 1
            break

    if blocked < 4:
        p1 += 1
    p2 = max(p2, math.prod(score))

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
