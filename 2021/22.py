#!/usr/bin/env python3

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
        cmd = line.strip().split()[0]
        inp.append([cmd] + list(map(int, re.findall(r'-?[0-9]+', line))))

# Part 1
def run(lim):
    grid = {}
    for i, line in enumerate(inp):
        print(f'\r {i+1}/{len(inp)}', end='')
        cmd = line[0]
        for x in range(max(line[1], -lim), min(line[2], lim) + 1):
            for y in range(max(line[3], -lim), min(line[4], lim) + 1):
                for z in range(max(line[5], -lim), min(line[6], lim) + 1):
                    if cmd == 'on':
                        grid[x, y, z] = 1
                    else:
                        try:
                            grid.pop((x, y, z))
                        except KeyError:
                            pass
    return grid

p1 = sum(run(50).values())
print(f'\rPart 1: {p1}')

# Part 2

print(f'\rPart 2: {p2}')
