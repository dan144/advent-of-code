#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

dest = (7,4) if test else (31,39)

mx, my = dest[0] * 2, dest[1] * 2

inp = []
with open(input_file) as f:
    num = int(f.readline().rstrip())

grid = {}
for x in range(mx):
    for y in range(my):
        v = x*x + 3*x + 2*x*y + y + y*y + num
        b = bin(v)[2:]
        grid[x, y] = b.count('1') % 2 == 0
        # open: True, wall: False

adjs = {(-1, 0), (1, 0), (0, -1), (0, 1)}

def find_dist(grid, dist, locs, dest, visited=None):
    if dist <= 50 and visited is not None:
        visited.update(locs)

    new_froms = set()
    for loc in locs:
        x, y = loc
        for dx, dy in adjs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < mx and 0 <= ny < my:
                if (nx, ny) == dest:
                    return dist + 1
                if grid[nx, ny]:
                    new_froms.add((nx, ny))
    if new_froms:
        return find_dist(grid, dist + 1, new_froms, dest, visited)
    return -1

p1 = find_dist(grid, 0, {(1, 1)}, dest)
print(f'Part 1: {p1}')

visited = set()
try:
    find_dist(grid, 0, {(1, 1)}, (mx - 1, my - 1), visited)
except:
    p2 = len(visited)
    print(f'Part 2: {p2}')
    #raise
