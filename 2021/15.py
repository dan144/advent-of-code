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
def find_cheapest(grid):
    min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)

    # assumes top left to bottom right
    start = (min_y, min_x)
    end = (max_y, max_x)

    locs = {start}
    costs = {start: 0}

    while locs: # search until no change in grid
        n_locs = set()
        for y, x in locs:
            for dx, dy in utils.adjs:
                nx = x + dx
                ny = y + dy
                if (ny, nx) not in grid:
                    continue
                cost = costs.get((y, x), float('inf')) + grid[ny, nx]
                if cost <= costs.get((ny, nx), float('inf')):
                    # if cheaper this way, update cost and reconsider this point
                    costs[ny, nx] = cost
                    n_locs.add((ny, nx))
        locs = n_locs

    return costs[end]

p1 = find_cheapest(grid)
print(f'Part 1: {p1}')

# Part 2

# expand grid
min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
dx = max_x - min_x + 1
dy = max_y - min_y + 1
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

p2 = find_cheapest(grid)
print(f'Part 2: {p2}')
