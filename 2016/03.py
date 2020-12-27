#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(list(map(int, line.rstrip().split())))

for sides in inp:
    sides = sorted(sides)
    p1 += sum(sides[:2]) > sides[2]

print(f'Part 1: {p1}')

for i in range(0, len(inp), 3):
    for j in range(3):
        sides = []
        for k in range(3):
            sides.append(inp[i+k][j])
        print(sides)
        sides = sorted(sides)
        p2 += sum(sides[:2]) > sides[2]

print(f'Part 2: {p2}')
