#!/usr/bin/env python3

import re
import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

dots = {}
with open(input_file) as f:
    for line in f:
        dot = tuple(map(int, re.findall(r'\d+', line.strip())))
        dots[dot] = '.'

# Part 1
adjs = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1)
)

mnx = float('inf')
mny = float('inf')
mnz = float('inf')
mxx = 0
mxy = 0
mxz = 0

for x, y, z in dots:
    mnx = min(x, mnx)
    mny = min(y, mny)
    mnz = min(z, mnz)

    mxx = max(x, mxx)
    mxy = max(y, mxy)
    mxz = max(z, mxz)

    for dx, dy, dz in adjs:
        if dots.get((x + dx, y + dy, z + dz)) is None:
            p1 += 1

print(f'Part 1: {p1}')

# Part 2

def flood_fill(dots, locs):
    new_locs = set()
    for x, y, z in locs:
        dots[x, y, z] = '.'
        for dx, dy, dz in adjs:
            nx, ny, nz = x + dx, y + dy, z + dz
            if not mnx <= nx <= mxx or not mny <= ny <= mxy or not mnz <= nz <= mxz:
                continue

            if dots.get((nx, ny, nz)) is None:
                new_locs.add((nx, ny, nz))

    if new_locs:
        flood_fill(dots, new_locs)
    return dots

mnx -= 1
mny -= 1
mnz -= 1
mxx += 1
mxy += 1
mxz += 1
filled = flood_fill(deepcopy(dots), {(mnx, mny, mnz)})

p2 = p1
for x, y, z in dots:
    for dx, dy, dz in adjs:
        nx, ny, nz = x + dx, y + dy, z + dz
        if filled.get((nx, ny, nz)) is None:
            p2 -= 1

print(f'Part 2: {p2}')
