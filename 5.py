#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file, 'r') as f:
    for line in f:
        inp.append(line)

ids = []
for line in inp:
    mn = 0
    mx = 127
    for i in range(7):
        c = line[i]
        l = mx - mn + 1
        l //= 2
        if c == 'F':
            # lower half
            mx -= l
        else:
            mn += l
    row = mn

    mn = 0
    mx = 7
    for i in range(3):
        c = line[i+7]
        l = mx - mn + 1
        l //= 2
        if c == 'L':
            mx -= l
        else:
            mn += l
    col = mn
    seat = row * 8 + col

    p1 = max(p1, seat)

    ids.append(seat)

print(f'Part 1: {p1}')

ids = sorted(ids)
for i in range(len(ids) - 1):
    if ids[i] + 1 != ids[i+1]:
        p2 = ids[i] + 1

print(f'Part 2: {p2}')
