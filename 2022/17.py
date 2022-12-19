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
        jets = list(line.strip())

# Part 1

shape_coords = (
    (
        (3, 4), (4, 4), (5, 4), (6, 4)
    ), (
        (3, 5), (4, 5), (5, 5), (4, 4), (4, 6)
    ), (
        (3, 4), (4, 4), (5, 4), (5, 5), (5, 6)
    ), (
        (3, 4), (3, 5), (3, 6), (3, 7)
    ), (
        (3, 4), (4, 4), (3, 5), (4, 5)
    )
)

grid = {}
for y in range(1, 8):
    grid[y, 0] = '-'
grid[0, 0] = '+'
grid[8, 0] = '+'

moveidx = 0
for b in range(2022):
    min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
    new_coords = list(map(list, shape_coords[b % 5]))
    for c in new_coords:
        c[1] += max_y

    while True:
        move = jets[moveidx % len(jets)]
        moveidx += 1

        # sideways
        can_move = True
        for (x, y) in new_coords:
            if move == '<':
                x -= 1
            else:
                x += 1
            if x in {0, 8} or grid.get((x, y)):
                can_move = False
                break
        if can_move:
            for c in new_coords:
                c[0] += 1 if move == '>' else -1

        # down
        can_move = True
        for (x, y) in new_coords:
            if grid.get((x, y-1)):
                can_move = False
                break
        for c in new_coords:
            if can_move:
                c[1] -= 1
            else:
                grid[tuple(c)] = '#'
        if not can_move:
            break

_, _, _, p1 = utils.get_grid_edges(grid)
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')