#!/usr/bin/env python3

from blist import blist

import itertools
import re
import sys

from copy import copy

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
    inp = blist(utils.load_comma_sep_nums(f)) # 1,2,3,...

nums = {}
for v in sorted(inp):
    nums[v] = nums.get(v, 0) + 1

# Part 1
for day in range(80):
    s = len(inp)
    for i in range(len(copy(inp))):
        if inp[i] == 0:
            inp.append(8)
            inp[i] = 6
        else:
            inp[i] -= 1
    #print(day, len(inp), len(inp) - s)

p1 = len(inp)
print(f'Part 1: {p1}')

# Part 2
for day in range(256):
    new = nums.get(0, 0)
    for l in range(8):
        nums[l] = nums.get(l+1, 0)
    nums[8] = new
    nums[6] += new
p2 = sum(nums.values())
print(f'Part 2: {p2}')
