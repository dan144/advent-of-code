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
    grid = utils.load_grid(f, str) # 2D grid of X type

# Part 1
start = set()
for loc, v in grid.items():
    if v in 'Sa':
        start.add(loc)
    elif v == 'E':
        end = loc

def find_dist(grid, dist, dist_grid, locs, dest):
    # recursively find distance (initially 0) from locs (initially source) to dest
    # locs is set(x,y tuple), dest is x,y tuple
    new_froms = set()
    for x, y in locs:
        my_space = grid[x, y]
        dist_grid[x, y] = dist
        for dx, dy in utils.adjs:
            nx, ny = x + dx, y + dy
            neighbor = grid.get((nx, ny))
            if neighbor is not None:
                print(f'{dist} grid[{x}, {y}]={my_space} grid[{nx}, {ny}]={neighbor}')
                print(ord(my_space), ord(neighbor))
                if ord(neighbor) <= ord(my_space) + 1 and dist < dist_grid.get((nx, ny), float('inf')):
                    if (nx, ny) == dest:
                        return dist + 1
                    print('adding')
                    new_froms.add((nx, ny))
    print(new_froms)
    #input()
    if new_froms:
        return find_dist(grid, dist + 1, dist_grid, new_froms, dest)
    return -1

print(start, end)
for x in start:
    grid[x] = 'a'
grid[end] = 'z'
utils.display_grid(grid)
p1 = find_dist(grid, 0, {}, start, end)
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
