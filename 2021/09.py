#!/usr/bin/env python3

from copy import copy

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

inp = []
with open(input_file) as f:
    inp = utils.load_grid(f, int) # 2D grid

# Part 1
lows = set()
for (x, y), v in inp.items():
    valid = True
    for dx, dy in utils.adjs:
        if inp.get((x+dx, y+dy), float('inf')) <= v: # neighbor is lower than this spot
            valid = False
            break
    if valid:
        p1 += 1 + v
        lows.add((x, y))
print(f'Part 1: {p1}')

# Part 2
basins = []
for low in lows:
    locs = {low}
    old_len = 0
    while len(locs) != old_len: # i.e. you added another x,y to this basin
        old_len = len(locs)
        for (x, y) in copy(locs):
            for dx, dy in utils.adjs:
                check = x + dx, y + dy
                if inp.get(check, 9) < 9:
                    locs.add(check)
    basins.append(len(locs))

basins = sorted(basins, reverse=True)
p2 = basins[0] * basins[1] * basins[2]
print(f'Part 2: {p2}')
