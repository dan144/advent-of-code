#!/usr/bin/env python3

import sys

import utils
# display_grid((y, x) grid) - display values in 2D map grid
# adjs - set of dx,dy values for LRUD adjacencies

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    grid = utils.load_grid(f, str) # 2D grid of X type

def find_dist(grid, dist, dist_grid, locs, dest):
    # recursively find distance (initially 0) from locs (initially source) to dest
    # adapted from utils.py; neighbor only accepted if close enough
    new_froms = set()
    for x, y in locs:
        my_space = grid[x, y]
        dist_grid[x, y] = dist
        for dx, dy in utils.adjs:
            nx, ny = x + dx, y + dy
            neighbor = grid.get((nx, ny))
            if neighbor is not None:
                #print(f'{dist} grid[{x}, {y}]={my_space} grid[{nx}, {ny}]={neighbor}')
                if ord(neighbor) <= ord(my_space) + 1 and dist < dist_grid.get((nx, ny), float('inf')):
                    if (nx, ny) == dest:
                        return dist + 1
                    new_froms.add((nx, ny))
    if new_froms:
        return find_dist(grid, dist + 1, dist_grid, new_froms, dest)
    return -1

# Part 1
for loc, v in grid.items():
    if v == 'S':
        start = loc
    elif v == 'E':
        end = loc

grid[start] = 'a'
grid[end] = 'z'
p1 = find_dist(grid, 0, {}, {start}, end)
print(f'Part 1: {p1}')

# Part 2
start = set()
for loc, v in grid.items():
    if v == 'a':
        start.add(loc)
p2 = find_dist(grid, 0, {}, start, end)
print(f'Part 2: {p2}')
