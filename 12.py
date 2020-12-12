#!/usr/bin/env python3

import re
import sys

from computer import parse, run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append((line[0], int(line[1:])))

dirs = 'NESW'
direc = 1
y = 0
x = 0
wy = 10
wx = 1
for act, dist in inp:
    if act == 'R':
        direc = (direc + (dist // 90)) % 4
        act = dirs[direc]
    elif act == 'L':
        direc = (direc - (dist // 90)) % 4
        act = dirs[direc]
    else:
        if act == 'F':
            act = dirs[direc]
        if act == 'N':
            y += dist
        elif act == 'S':
            y -= dist
        elif act == 'E':
            x += dist
        elif act == 'W':
            x -= dist

p1 = abs(x) + abs(y)
print(f'Part 1: {p1}')

direc = 1
y = 0
x = 0
wy = 1
wx = 10
for act, dist in inp:
    if act == 'R' or act == 'L':
        turns = dist // 90
        for t in range(turns):
            if act == 'R':
                s = wy
                wy = -1 * wx
                wx = s
            else:
                s = wx
                wx = -1 * wy
                wy = s
    elif act == 'F':
        x += dist * wx
        y += dist * wy

    elif act == 'N':
        wy += dist
    elif act == 'S':
        wy -= dist
    elif act == 'E':
        wx += dist
    elif act == 'W':
        wx -= dist

p2 = abs(x) + abs(y)
print(f'Part 2: {p2}')
