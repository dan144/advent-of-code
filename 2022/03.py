#!/usr/bin/env python3

import string
import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# find_cheapest(grid, (y,x) start, (y,x) end) - grid of ints, finds cheapest path from start to end, returns cost dist
# transpose_grid(grid) - swap key values from (x, y) to (y, x) and back
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
    for line in f:
        inp.append(line.strip())

# Part 1
for sack in inp:
    l = len(sack)
    f, s = set(sack[:l//2]), set(sack[l//2:])
    same = (f & s).pop()
    print(same)
    if same in string.ascii_lowercase:
        p1 += string.ascii_lowercase.index(same) + 1
    elif same in string.ascii_uppercase:
        p1 += string.ascii_uppercase.index(same) + 27

print(f'Part 1: {p1}')

# Part 2
i = 0
sacks = []
for sack in inp:
    i += 1
    sacks.append(set(sack))
    if i == 3:
        same = sacks.pop()
        while sacks:
            same = same & sacks.pop()
        same = same.pop()
        print(same)
        if same in string.ascii_lowercase:
            p2 += string.ascii_lowercase.index(same) + 1
        elif same in string.ascii_uppercase:
            p2 += string.ascii_uppercase.index(same) + 27
        i = 0

print(f'Part 2: {p2}')
