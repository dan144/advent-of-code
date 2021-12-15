#!/usr/bin/env python3

import itertools
import re
import sys

from copy import deepcopy

import utils
### available functions:
# get_grid_edges: min_x, min_y, max_x, max_y
# display_grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime
# adjs - set of dx,dy values for LRUD adjacencies
# diags - set of dx,dy values for diagonals
# all_dirs set of dx,dy values for all 8 surrounding values

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    grid = utils.load_grid(f, int) # 2D grid of X type

# Part 1

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
start = (min_y, min_x)
end = (max_y, max_x)

locs = {start}
costs = {start: 0}

while locs or len(costs.values()) < len(grid.values()):
    n_locs = set()
    for y, x in locs:
        for dx, dy in utils.adjs:
            nx = x + dx
            ny = y + dy
            if (ny, nx) not in grid:
                continue
            cost = costs.get((y, x), float('inf')) + grid[ny, nx]
            if cost <= costs.get((ny, nx), float('inf')):
                costs[ny, nx] = cost
                n_locs.add((ny, nx))
    locs = n_locs

p1 = costs[end]
print(f'Part 1: {p1}')

# Part 2
dx = max_x - min_x + 1
dy = max_y - min_y + 1
og = deepcopy(grid)
for mx in range(5):
    for my in range(5):
        if mx == my == 0:
            continue
        for (y, x), v in og.items():
            nx = mx * dx + x
            ny = my * dy + y
            nv = (v + mx + my)
            if nv > 9:
                nv -= 9
            grid[ny, nx] = nv

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
start = (min_y, min_x)
end = (max_y, max_x)

locs = {start}
costs = {start: 0}

while locs or len(costs.values()) < len(grid.values()):
    n_locs = set()
    for y, x in locs:
        for dx, dy in utils.adjs:
            nx = x + dx
            ny = y + dy
            if (ny, nx) not in grid:
                continue
            cost = costs.get((y, x), float('inf')) + grid[ny, nx]
            if cost <= costs.get((ny, nx), float('inf')):
                costs[ny, nx] = cost
                n_locs.add((ny, nx))
    locs = n_locs

p2 = costs[end]
print(f'Part 2: {p2}')
