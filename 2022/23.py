#!/usr/bin/env python3

import itertools
import re
import sys

from copy import deepcopy

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
def east():
    move = True
    for dx in (-1, 0, 1):
        if grid.get((x + dx, y - 1), '.') == '#':
            move = False
    if move:
       return ((x, y), (x, y - 1))

def west():
    move = True
    for dx in (-1, 0, 1):
        if grid.get((x + dx, y + 1), '.') == '#':
            move = False
    if move:
        return ((x, y), (x, y + 1))

def north():
    move = True
    for dy in (-1, 0, 1):
        if grid.get((x - 1, y + dy), '.') == '#':
            move = False
    if move:
        return ((x, y), (x - 1, y))

def south():
    move = True
    for dy in (-1, 0, 1):
        if grid.get((x + 1, y + dy), '.') == '#':
            move = False
    if move:
        return ((x, y), (x + 1, y))

move_fxn = [north, south, east, west]
i = 0
new_grid = {}
removed = set()
while True:
    i += 1
    print(f'\r{i}', end='')
    if test:
        if grid:
            utils.display_grid(grid, '.')
            input()

    moves = set()
    for (x, y), v in grid.items():
        if v == '.': # nothing
            continue
        for dx, dy in utils.all_dirs:
            nx, ny = x + dx, y + dy
            v = grid.get((nx, ny), '.')
            if v == '#':
                break
        else:
            moves.add(((x, y), (x, y)))
            continue # found no elves

        for f in range(4):
            if (n := move_fxn[f]()):
                moves.add(n)
                break
        else:
            moves.add(((x, y), (x, y))) # can't move any direction

    move_fxn = move_fxn[1:] + [move_fxn[0]]

    new_grid = {}
    for p, np in moves:
        if p == np: # didn't move, stay in place
            new_grid[p] = '#'
            continue
        for p2, np2 in moves:
            if p == p2:
                continue
            if np == np2: # crash, don't move
                new_grid[p] = '#'
                break
        else: # didn't crash
            new_grid[np] = '#'
    if grid == new_grid:
        break
    grid = new_grid
    if i == 10 or new_grid is {}:
        ngrid = deepcopy(grid)
        for x, y in removed:
            ngrid[x, y] = '#'
        min_x, min_y, max_x, max_y = utils.get_grid_edges(ngrid)
        p1 = (max_x - min_x + 1) * (max_y - min_y + 1) - len(ngrid.keys())
        print(f'Part 1: {p1}')

p2 = i
print(f'Part 2: {p2}')
