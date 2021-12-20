#!/usr/bin/env python3

import sys

from copy import deepcopy

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid
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
    # all . values (i.e. the "infinite" border) will use the first bit of the image enhanacement alg
    # if the first value in inp is '#' then they'll become 1
    # if the last value in inp is '.' then they'll flip back
    if inp[0] == '#':
        return inp[0] if s % 2 else inp[-1]
    return inp[0]

# Part 1
def run(grid, n):
    for s in range(n):
        d = default_val(s)
        n = {}

        # ensure doing all neighbors to handle "infinite"
        mnx, mny, mxx, mxy = utils.get_grid_edges(grid)
        mnx -= 1
        mny -= 1
        mxx += 1
        mxy += 1
        for x in range(mnx, mxx + 1):
            for y in range(mny, mxy + 1):
                v = ''
                for (dy, dx) in sorted(utils.all_dirs | {(0, 0)}):
                    ny = y + dy
                    nx = x + dx
                    v += grid.get((ny, nx), d)
                v = v.replace('#', '1').replace('.', '0')
                v = int(v, 2)
                n[y, x] = inp[v]
        grid = n
    return grid

g = run(deepcopy(grid), 2)
p1 = sum((x == '#' for x in g.values()))
print(f'Part 1: {p1}')

# Part 2
g = run(deepcopy(grid), 50)
p2 = sum((x == '#' for x in g.values()))
print(f'Part 2: {p2}')
