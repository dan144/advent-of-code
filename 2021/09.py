#!/usr/bin/env python3

from copy import copy
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
    inp = utils.load_grid(f) # 2D grid

# Part 1
lows = set()
for (x, y), v in inp.items():
    valid = True
    for dx, dy in {(-1, 0), (0, -1), (1, 0), (0, 1)}:
        n = inp.get((x+dx, y+dy), float('inf'))
        if float(n) <= float(v):
            valid = False
    if valid:
        p1 += 1 + int(v)
        lows.add((x,y))
print(f'Part 1: {p1}')

# Part 2
basins = []
for low in lows:
    locs = set((low,))
    old_len = 0
    while len(locs) != old_len:
        old_len = len(locs)
        for (x, y) in copy(locs):
            for dx, dy in {(-1, 0), (0, -1), (1, 0), (0, 1)}:
                v = int(inp.get((x+dx, y+dy), 9))
                if v < 9:
                    locs.add((x+dx, y+dy))
    basins.append(len(locs))
basins = sorted(basins, reverse=True)
p2 = basins[0] * basins[1] * basins[2]
print(f'Part 2: {p2}')
