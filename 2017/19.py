#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = ''
p2 = 0

with open(input_file) as f:
    grid = utils.load_grid(f)

_, _, mxx, mxy = utils.get_grid_edges(grid)
for y in range(mxy + 1):
    if grid[0, y] == '|':
        sy = y
        break

x, y = 0, sy
dx, dy = 1, 0

# go until you're off the path
while grid.get((x, y), ' ') != ' ':
    x += dx
    y += dy
    p2 += 1 # count steps

    if grid[x, y] == '+':
        # turn
        if dx == 0:
            dy = 0
            # check if move left is illegal
            if grid.get((x - 1, y), ' ') in ' -':
                dx = 1
            else:
                dx = -1
        else:
            dx = 0
            # check if move up is illegal
            if grid.get((x, y - 1), ' ') in ' |':
                dy = 1
            else:
                dy = -1
    elif grid[x, y] not in '-|':
        # not a normal space (i.e. letter)
        p1 += grid[x, y]

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
