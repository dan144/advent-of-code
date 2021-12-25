#!/usr/bin/env python3

import sys

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y - learned today this isn't true for y,x keyed grids
# display_grid((y, x) grid) - display values in 2D map grid

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

grid = []
with open(input_file) as f:
    grid = utils.load_grid(f, str) # 2D grid of X type

# Part 1
_, _, max_y, max_x = utils.get_grid_edges(grid)
max_y += 1
max_x += 1
again = True
while again:
    again = False
    p1 += 1
    for can_move in '>v':
        new = {}
        for (y, x), v in grid.items():
            if v != can_move:
                continue

            if v == 'v':
                ny = (y + 1) % max_y
                nx = x
            elif v == '>':
                nx = (x + 1) % max_x
                ny = y
            else:
                assert v == '.'
                continue

            if grid[ny, nx] == '.':
                new[y, x] = '.'
                new[ny, nx] = v

        if new:
            again = True
        grid.update(new)
    print(f'\rStep {p1}', end='')
print(f'\rPart 1: {p1}')
