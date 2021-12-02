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
x, y = 0, 0
for direc, m in inp:
    if direc == 'forward':
        x += int(m)
    else:
        if direc == 'down':
            y += int(m)
        else:
            y -= int(m)
p1 = x * y
print(f'Part 1: {p1}')

# Part 2
x, y = 0, 0
aim = 0
for direc, m in inp:
    if direc == 'forward':
        x += int(m)
        y += aim * int(m)
    else:
        if direc == 'down':
            aim += int(m)
        else:
            aim -= int(m)
p2 = x * y
print(f'Part 2: {p2}')
