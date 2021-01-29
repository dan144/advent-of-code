#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    grid = utils.load_grid(f)

CLEAN = 0
WEAK = 1
INFECTED = 2
FLAGGED = 3
grid2 = {}
for (x, y), v in grid.items():
    grid2[x, y] = CLEAN if v == '.' else INFECTED

directions = 'NESW'
moves = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

mnx, mny, mxx, mxy = utils.get_grid_edges(grid)

x = (mxx - mnx) // 2
y = (mxy - mny) // 2

direction = 0
for burst in range(10000):
    if grid.get((x, y), '.') == '#':
        direction = (direction + 1) % len(directions)
        grid[x, y] = '.'
    else:
        direction = (direction - 1) % len(directions)
        grid[x, y] = '#'
        p1 += 1
    dy, dx = moves[directions[direction]]
    x += dx
    y += dy

print(f'Part 1: {p1}')

direction = 0
x = (mxx - mnx) // 2
y = (mxy - mny) // 2
for burst in range(10000000):
    if burst % 100000 == 0:
        print(f'\r{burst}', end='')
    spot = grid2.get((x, y), CLEAN)
    if spot == CLEAN:
        direction = (direction - 1) % len(directions)
        grid2[x, y] = WEAK
    elif spot == WEAK:
        grid2[x, y] = INFECTED
        p2 += 1
    elif spot == INFECTED:
        direction = (direction + 1) % len(directions)
        grid2[x, y] = FLAGGED
    elif spot == FLAGGED:
        direction = (direction + 2) % len(directions)
        grid2[x, y] = CLEAN
    dy, dx = moves[directions[direction]]
    x += dx
    y += dy

print(f'\nPart 2: {p2}')
