#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line[:-1])

poss_moves = {'e', 'se', 'sw', 'w', 'nw', 'ne'}
change = {
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
}
tiles = {}

for line in inp:
    moves = re.findall('|'.join(poss_moves), line)
    x, y = 0, 0
    for move in moves:
        dx, dy = change[move]
        x += dx
        y += dy
    if (x, y) not in tiles:
        tiles[x, y] = True # black
    else:
        tiles[x, y] = not tiles[x, y]
    for dx, dy in change.values():
        nx, ny = x + dx, y + dy
        if (nx, ny) not in tiles:
            tiles[nx, ny] = False

p1 = sum(tiles.values())
print(f'Part 1: {p1}')

for day in range(100):
    new = {}
    for (x, y), state in tiles.items():
        adj = 0
        for (dx, dy) in change.values():
            nx, ny = x + dx, y + dy
            neighbor = tiles.get((nx, ny), False)
            adj += neighbor is True

        assert (x, y) not in new
        if state is True and (adj == 0 or adj > 2):
            new[x, y] = False
        elif state is False and adj == 2:
            new[x, y] = True
        else:
            new[x, y] = state

    for (x, y) in list(new.keys()):
        for dx, dy in change.values():
            nx, ny = x + dx, y + dy
            if (nx, ny) not in new:
                new[nx, ny] = False

    tiles = new
    print(f'\rDay {day + 1}: {sum(tiles.values())}', end='')

p2 = sum(tiles.values())
print()
print(f'Part 2: {p2}')
