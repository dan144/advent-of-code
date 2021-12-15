#!/usr/bin/env python3

import sys

import utils
# get_grid_edges: min_x, min_y, max_x, max_y
# display_grid
# adjs - set of dx,dy values for LRUD adjacencies

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    grid = utils.load_grid(f, int) # 2D grid of X type

# Part 1
min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
start = (min_y, min_x)
end = (max_y, max_x)
p1 = utils.find_cheapest(grid, start, end)[end]
print(f'Part 1: {p1}')

# Part 2
dx = max_x - min_x + 1
dy = max_y - min_y + 1

# expand grid
for y, x in set(grid.keys()):
    for mx in range(5):
        for my in range(5):
            if mx == my == 0:
                continue # not strictly necessary, but a little faster
            nx = mx * dx + x
            ny = my * dy + y
            nv = (grid.get((y, x)) + mx + my)
            if nv > 9: # wrap around to 1 after 9
                nv -= 9
            grid[ny, nx] = nv

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
start = (min_y, min_x)
end = (max_y, max_x)
p2 = utils.find_cheapest(grid, start, end)[end]
print(f'Part 2: {p2}')
