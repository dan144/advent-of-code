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

ids = set()
for line in inp:
    row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(line[7:].replace('L', '0').replace('R', '1'), 2)
    seat = row * 8 + col

    p1 = max(p1, seat)

    ids.add(seat)

print(f'Part 1: {p1}')

p2 = (set(range(min(ids), max(ids) + 1)) - ids).pop()
print(f'Part 2: {p2}')
