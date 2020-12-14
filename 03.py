#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 1

inp = {}
with open(input_file, 'r') as f:
    y = 0
    for line in f:
        for x, c in enumerate(line):
            inp[(y, x)] = c
        y += 1

width = len(line) - 1

def check_slope(dx, dy):
    c = 0
    x = 0
    y = 0
    while y < len(inp):
        y += dy
        x += dx
        if inp.get((y, x % width)) == '#':
            c += 1
    return c


p1 = check_slope(3, 1)
print(f'Part 1: {p1}')


for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    p2 *= check_slope(*slope)
print(f'Part 2: {p2}')
