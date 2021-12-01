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
    for line in f:
        pass # if need custom
    inp = utils.load_num_lines(f) # one int per line
    inp = utils.load_comma_sep_nums(f) # 1,2,3,...
    inp = utils.load_split_lines(f) # asdf asdf asdf ...
    inp = utils.load_one_line_of_nums(f) # 1 2 3 ...
    inp = utils.load_grid(f) # 2D grid

# Part 1

print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
