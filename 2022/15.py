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
pairs = []
specials = set()
with open(input_file) as f:
    for line in f:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        pairs.append(((sx, sy), (bx, by)))
        grid[sy, sx] = 'S'
        grid[by, bx] = 'B'
        specials.add((sx, sy))
        specials.add((bx, by))

# Part 1

for s, b in pairs:
    sx, sy = s
    bx, by = b
    d = utils.manh(s, b)
    print(s, b, d)
    grid[sy + d, sx] = '.'
    grid[sy - d, sx] = '.'
    grid[sy, sx + d] = '.'
    grid[sy, sx - d] = '.'

    #for x in range(-1 * d, d + 1):
    #    for y in range(-1 * d, d + 1):
    #        if abs(x) + abs(y) <= d:
    #            c = sy + y, sx + x
    #            if grid.get(c) is None:
    #                #grid[c] = '#'
    #                if sy + y == (10 if test else 2000000):
    #                    p1 += 1
    #                    print(p1)
    #if test:
    #    utils.display_grid(grid)
    #    input()
#min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
#dx = max_x - min_x
#y = 10 if test else 2000000
#for x in range(min_x, max_x + 1):
#    if grid.get((y, x)) == '#':
#        p1 += 1

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
print(min_x, min_y, max_x, max_y)
if test:
    utils.display_grid(grid)

y = 10 if test else 2000000
for x in range(min_x, max_x + 1):
    for s, b in pairs:
        d = utils.manh(s, b)
        if utils.manh(s, (x, y)) <= d and (x, y) not in specials:
            p1 += 1
            if test:
                print(p1, (x, y))
            else:
                print(f'\r{p1}  ', end='')
            break

# not 5665305
# not 5665304
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
