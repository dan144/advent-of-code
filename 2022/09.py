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
        inp.append(line.strip())

# Part 1

head = [0, 0]
tail = [0, 0]
tail_pos = {(0, 0)}
for line in inp:
    d, dist = line.split()
    dist = int(dist)
    for step in range(dist):
        # move head
        if d == 'R':
            head[0] += 1
        elif d == 'L':
            head[0] -= 1
        elif d == 'U':
            head[1] += 1
        elif d == 'D':
            head[1] -= 1
        else:
            assert False

        # move tail?
        dx = tail[0] - head[0]
        dy = tail[1] - head[1]
        if abs(dx) > 1 or abs(dy) > 1:
            if dx != 0:
                tail[0] -= 1 if (dx > 0) else -1
            if dy != 0:
                tail[1] -= 1 if (dy > 0) else -1
        #if dx > 1:
        #    tail[0] -= 1
        #elif dx < -1:
        #    tail[0] += 1
        #if dy > 1:
        #    tail[1] -= 1
        #elif dy < -1:
        #    tail[1] += 1

        tail_pos.add(tuple(tail))

        #grid = {}
        #for pos in tail_pos:
        #    grid[pos] = '#'
        #grid[tuple(head)] = 'H'
        #grid[tuple(tail)] = 'T'
        #grid = utils.transpose_grid(grid)
        #utils.display_grid(grid)
        #input()

p1 = len(tail_pos)
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
