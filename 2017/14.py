#!/usr/bin/env python3

import sys

import utils

from knot import compute

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    inp = f.readline().rstrip()

grid = {}
for y in range(128):
    s = f'{inp}-{y}'
    h = compute(s)
    b = bin(int(h, 16))[2:]
    while len(b) < 128:
        b = '0' + b
    for x, c in enumerate(b):
        if c == '1':
            grid[x, y] = True

p1 = len(grid.values())
print(f'Part 1: {p1}')

def remove_group(grid):
    start = list(grid.keys())[0]
    grid.pop(start)
    in_group = {start}
    while in_group:
        neighbors = set()
        for x, y in in_group:
            for dx, dy in utils.adjs:
                neighbor = x + dx, y + dy
                if neighbor in grid:
                    grid.pop(neighbor)
                    neighbors.add(neighbor)
        in_group = neighbors

p2 = 0
while grid:
    p2 += 1
    remove_group(grid)

print(f'Part 2: {p2}')
