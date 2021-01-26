#!/usr/bin/env python3

import sys

p2 = 0

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    inp = f.readline().rstrip().split(',')

# moves in a hex grid
change = {
    'sw': (-1, -1),
    'se': (1, -1),
    's': (0, -2),
    'nw': (-1, 1),
    'ne': (1, 1),
    'n': (0, 2),
}

x, y = 0, 0
all_spots = set()
for move in inp:
    dx, dy = change[move]
    x += dx
    y += dy
    all_spots.add((x, y))

distances = {(0, 0): 0}
check_at = {(0, 0)}
dist = 0
while all_spots:
    dist += 1
    print(f'\rChecking dist {dist}', end='')
    next_check = set()
    for mx, my in check_at:
        for dx, dy in change.values():
            nx, ny = mx + dx, my + dy
            if (nx, ny) in distances:
                continue
            distances[nx, ny] = dist
            if x == nx and y == ny:
                print(f'\nPart 1: {dist}')
            if (nx, ny) in all_spots:
                all_spots.remove((nx, ny))
                p2 = max(p2, dist)
            next_check.add((nx, ny))
    check_at = next_check

print(f'\nPart 2: {p2}')
