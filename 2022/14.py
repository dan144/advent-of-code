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

grid = {}
with open(input_file) as f:
    for line in f:
        coords = line.split('->')
        prev = None
        for coord in coords:
            nx, ny = map(int, coord.strip().split(','))
            print(nx, ny)
            if prev is None:
                prev = (nx, ny)
                continue
            x, y = prev
            if x == nx and y != ny:
                dy = 1 if ny > y else -1
                for my in range(y, ny + dy, dy):
                    grid[my, x] = '#'
            elif y == ny and x != nx:
                dx = 1 if nx > x else -1
                for mx in range(x, nx + dx, dx):
                    grid[y, mx] = '#'
            else:
                assert x == nx and y == ny # single point; skip
            prev = (nx, ny)
        print()

min_y, min_x, max_y, max_x = utils.get_grid_edges(grid)
dx = max_x - min_x
max_y += 2

for x in range(min_x - 10 * dx, max_x + 10 * dx):
    grid[max_y, x] = '#'
grid[0, 500] = '+'
utils.display_grid(grid)


# Part 1

infinity = False
while not infinity:
    grain = (0, 500)
    falling = True
    while falling:
        if grain[0] >= max_y:
            # reached infinity
            infinity = True
            break
        dya = [0, -1, 1]
        for dy in dya:
            n = (grain[0] + 1, grain[1] + dy)
            if grid.get(tuple(n), '.') not in '#o':
                grain = n
                break # can fall this way
        else:
            grid[grain] = 'o'
            p1 += 1
            falling = False
    if grid.get((0, 500)) == 'o':
        infinity = True

print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
