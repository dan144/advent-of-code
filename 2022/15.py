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
        d = utils.manh((sx, sy), (bx, by))
        pairs.append(((sx, sy), (bx, by), d))
        grid[sy, sx] = 'S'
        grid[by, bx] = 'B'
        specials.add((sx, sy))
        specials.add((bx, by))

# Part 1

for s, b, d in pairs:
    sx, sy = s
    bx, by = b
    #d = utils.manh(s, b)
    grid[sy + d, sx] = '.'
    grid[sy - d, sx] = '.'
    grid[sy, sx + d] = '.'
    grid[sy, sx - d] = '.'

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
print(min_x, min_y, max_x, max_y)
if test:
    utils.display_grid(grid)

#y = 10 if test else 2000000
#for x in range(min_x, max_x + 1):
#    for s, b, d in pairs:
#        #d = utils.manh(s, b)
#        if utils.manh(s, (x, y)) <= d and (x, y) not in specials:
#            p1 += 1
#            if test:
#                print(p1, (x, y))
#            else:
#                print(f'\r{p1}  ', end='')
#            break
#
#print(f'Part 1: {p1}')

# Part 2
mx = 20 if test else 4000000
my = 20 if test else 4000000

for s, b, dist in pairs:
    print(s, b)
    dist += 1
    sx, sy = s
    for d in range(0, dist):
        for dx, dy in utils.diags:
            x = sx + dx * d
            y = sy + dy * (dist - d)
            if 0 <= x <= mx and 0 <= y <= my:
                testb = (x, y)
                #assert utils.manh(s, testb) == dist
                valid = True
                for s2, b2, dist2 in pairs:
                    if s != s2:
                        if utils.manh(s2, testb) <= dist2:
                            valid = False
                            break
                if valid:
                    break
            if valid:
                break
    if valid:
        break
assert valid

p2 = 4000000 * x + y
print(f'Part 2: {p2}')
