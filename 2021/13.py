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

grid = {}
to_folds = False
folds = []
with open(input_file) as f:
    for line in f:
        if to_folds:
            v = line.strip().split()[2]
            d, v = v.split('=')
            v = int(v)
            folds.append((d, v))
        elif line == '\n':
            to_folds = True
        else:
            x, y = map(int, line.strip().split(','))
            grid[y, x] = '#'

# Part 1
for d, v in folds:
    n_grid = {}
    for (y, x), val in deepcopy(grid).items():
        if d == 'y': # fold up
            if y > v:
                dd = abs(y - v)
                n_y = y - 2 * dd
            else:
                n_y = y
            n_grid[n_y, x] = val
        else: # fold left
            if x > v:
                dd = abs(x - v)
                n_x = x - 2 * dd
            else:
                n_x = x
            n_grid[y, n_x] = val

    grid = n_grid
    if p1 == 0:
        p1 = len(grid.values())

print(f'Part 1: {p1}')

# Part 2
utils.display_grid(grid)
