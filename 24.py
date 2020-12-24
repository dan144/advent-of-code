#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    inp = {line[:-1] for line in f}

WHITE = False
BLACK = True
poss_moves = {'e', 'se', 'sw', 'w', 'nw', 'ne'}

# moves in a hex grid
change = {
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
}

def surround_all(grid):
    for (x, y) in list(grid.keys()):
        for dx, dy in change.values():
            nx, ny = x + dx, y + dy
            if (nx, ny) not in grid:
                grid[nx, ny] = WHITE

grid = {}
for line in inp:
    moves = re.findall('|'.join(poss_moves), line) # greedy regex
    x, y = 0, 0
    for move in moves:
        dx, dy = change[move]
        x += dx
        y += dy
    if (x, y) not in grid:
        grid[x, y] = BLACK
    else:
        grid[x, y] = not grid[x, y]

p1 = sum(grid.values())
print(f'Part 1: {p1}')

for day in range(100):
    surround_all(grid) # ensure all possible spaces that can flip are considered
    new_grid = {}
    for (x, y), state in grid.items():
        adj = sum(grid.get((x + dx, y + dy), WHITE) for (dx, dy) in change.values())
        if state is BLACK and (adj == 0 or adj > 2):
            new_grid[x, y] = WHITE
        elif state is WHITE and adj == 2:
            new_grid[x, y] = BLACK
        else:
            new_grid[x, y] = state

    grid = new_grid
    print(f'\rDay {day + 1}: {sum(grid.values())}', end='')
print()

p2 = sum(grid.values())
print(f'Part 2: {p2}')
