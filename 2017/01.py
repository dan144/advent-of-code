#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    inp = list(f.readline().rstrip())

for i, c in enumerate(inp):
    if c == inp[(i + 1) % len(inp)]:
        p1 += int(c)

print(f'Part 1: {p1}')

off = len(inp) // 2
for i, c in enumerate(inp):
    if c == inp[(i + off) % len(inp)]:
        p2 += int(c)

print(f'Part 2: {p2}')
