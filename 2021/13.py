#!/usr/bin/env python3

import sys

from copy import deepcopy

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

grid = {}
to_folds = False
folds = []
with open(input_file) as f:
    for line in f:
        if to_folds: # already switched
            v = line.strip().split()[2]
            d, v = v.split('=')
            v = int(v)
            folds.append((d, v))
        elif line == '\n':
            to_folds = True # switch from parsing dots to parsing folds
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
    if p1 == 0: # grab this value after the first fold
        p1 = len(grid.values())

print(f'Part 1: {p1}')

# Part 2
utils.display_grid(grid)
