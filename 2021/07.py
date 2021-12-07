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
    inp = utils.load_comma_sep_nums(f) # 1,2,3,...

# Part 1
mn = min(inp)
mx = max(inp)

for x in range(mn, mx+1):
    cost = 0
    for crab in inp:
        cost += abs(crab - x)
    if p1 == 0 or p1 > cost:
        p1 = cost
print(f'Part 1: {p1}')

# Part 2
for x in range(mn, mx+1):
    cost = 0
    for crab in inp:
        s_cost = abs(crab - x)
        for y in range(s_cost+1):
            cost += y
    if p2 == 0 or p2 > cost:
        print(x, cost)
        p2 = cost
print(f'Part 2: {p2}')
