#!/usr/bin/env python3

import re
import sys

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# diags - set of dx,dy values for diagonals

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

grid = {} # create grid to get x bounds
pairs = [] # maintain sensor-beacon pairs with Manhattan dist
specials = set() # list of all places that known things are
with open(input_file) as f:
    for line in f:
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        d = utils.manh((sx, sy), (bx, by))

        pairs.append(((sx, sy), (bx, by), d))
        specials.add((sx, sy))
        specials.add((bx, by))

        grid[sy, sx] = 'S'
        grid[by, bx] = 'B'

        # notes the cardinal direction bounds on the grid
        grid[sy + d, sx] = 'v'
        grid[sy - d, sx] = '^'
        grid[sy, sx + d] = '>'
        grid[sy, sx - d] = '<'

# Part 1

min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
if test:
    utils.display_grid(grid)

y = 10 if test else 2000000
no_change = 0
for x in range(min_x, max_x + 1):
    no_change += 1
    for s, b, d in pairs:
        if utils.manh(s, (x, y)) <= d and (x, y) not in specials:
            p1 += 1
            no_change = 0
            print(f'\r{p1}  ', end='')
            break
    if p1 > 0 and no_change > 1000:
        break # okay to quit once you see a swath of coords that are valid

print(f'\nPart 1: {p1}')

# Part 2
mx = 20 if test else 4000000
my = 20 if test else 4000000

valid = False
for s, b, dist in pairs:
    print(f'\rChecking {s}->{b}  ', end='')
    dist += 1
    sx, sy = s
    for d in range(0, dist):
        for dx, dy in utils.diags:
            x = sx + dx * d
            y = sy + dy * (dist - d)
            if 0 <= x <= mx and 0 <= y <= my:
                testb = (x, y)
                valid = True
                for s2, b2, dist2 in pairs:
                    # check the Manhattan dist from this potential answer to every other sensor
                    # if this dist is less than the sensor's distance to its beacon, it's not the place
                    if s != s2 and utils.manh(s2, testb) <= dist2:
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
print(f'\nPart 2: {p2}')
