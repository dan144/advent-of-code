#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    inp = [line[:-1] for line in f]

WHITE = False
BLACK = True
poss_moves = {'e', 'se', 'sw', 'w', 'nw', 'ne'}
re_moves = re.compile('|'.join(poss_moves))

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
    for x, y in list(grid.keys()):
        if grid[x, y] is WHITE:
            # white spaces' neighbors don't need to be added since they won't flip
            continue
        for dx, dy in change.values():
            nx, ny = x + dx, y + dy
            grid.setdefault((nx, ny), WHITE)

grid = {}
for line in inp:
    moves = re_moves.findall(line) # greedy regex
    x, y = map(sum, zip(*(change[move] for move in moves)))

    # try to flip the tile, set to default BLACK if not present
    try:
        grid[x, y] ^= True
    except KeyError:
        grid[x, y] = BLACK

p1 = sum(grid.values())
print(f'Part 1: {p1}')

for day in range(100):
    surround_all(grid) # ensure all possible spaces that can flip are considered
    flipped_tiles = {}
    for (x, y), state in grid.items():
        adj = sum(grid.get((x + dx, y + dy), WHITE) for (dx, dy) in change.values())
        if state is BLACK and (adj == 0 or adj > 2):
            flipped_tiles[x, y] = WHITE
        elif state is WHITE and adj == 2:
            flipped_tiles[x, y] = BLACK

    grid.update(flipped_tiles)
    print(f'\rDay {day + 1}: {sum(grid.values())}', end='')
print()

p2 = sum(grid.values())
print(f'Part 2: {p2}')
