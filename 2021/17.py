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

with open(input_file) as f:
    for line in f:
        inp = line.strip()


# target area: x=20..30, y=-10..-5
x1, x2, y1, y2 = map(int, re.findall(r'-?[0-9]+', line))
xl, xh = sorted((x1, x2))
yl, yh = sorted((y1, y2))

# Part 1
def do_step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return x, y, vx, vy

for v_y in range(150, yl-1, -1):
    for v_x in range(xh, 0, -1):
        vx = v_x
        vy = v_y

        max_y = 0
        x, y = 0, 0
        step = 0
        good = True
        while step < 10000:
            step += 1
            x, y, vx, vy = do_step(x, y, vx, vy)
            max_y = max(max_y, y)
            if x in range(xl, xh+1) and y in range(yl, yh+1):
                break
            if y < yl: # too low, will never make it
                good = False
                break
        else:
            good = False

        if good:
            p1 = max(p1, max_y)
            p2 += 1

print(f'Part 1: {p1}')

# Part 2
print(f'Part 2: {p2}')
