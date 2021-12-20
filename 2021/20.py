#!/usr/bin/env python3

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

inp = ''
inp_done = False
grid = {}
y = 0
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            inp_done = True
        elif not inp_done:
            inp = line
        else:
            for x, c in enumerate(line):
                grid[y, x] = c
            y += 1

def default_val(s):
    if test:
        return '.'
    return '#' if s % 2 else '.'
print(inp)
print()
# Part 1
def run(grid, n):
    for s in range(n):
        n = {}
        mnx, mny, mxx, mxy = utils.get_grid_edges(grid)
        mnx -= 1
        mny -= 1
        mxx += 1
        mxy += 1
        for x in range(mnx, mxx+1):
            for y in range(mny, mxy+1):
                v = ''
                for (dy, dx) in sorted(utils.all_dirs | {(0, 0)}):
                    ny = y + dy
                    nx = x + dx
                    v += grid.get((ny, nx), default_val(s))
                v = v.replace('#', '1').replace('.', '0')
                v = int(v, 2)
                n[y, x] = inp[v]
        grid = n
    return grid

#utils.display_grid(grid)
g = run(deepcopy(grid), 2)
p1 = sum((x == '#' for x in g.values()))
print(f'Part 1: {p1}')

# Part 2
g = run(deepcopy(grid), 50)
p2 = sum((x == '#' for x in g.values()))
print(f'Part 2: {p2}')
