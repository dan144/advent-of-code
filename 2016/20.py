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
        inp.append(line.rstrip())

ranges = []
for line in inp:
    mn, mx = map(int, line.split('-'))
    ranges.append([mn, mx])

ranges = sorted(ranges, key=lambda x: x[0])
for (mn, mx) in ranges:
    if not mn <= p1 <= mx:
        continue
    p1 = mx + 1

print(f'Part 1: {p1}')

for i in range(len(ranges)):
    mn, mx = ranges[i]
    for j, (mn2, mx2) in enumerate(ranges[i + 1:]):
        if mn2 <= mx:
            ranges[i + 1 + j][0] = mx + 1
    if mx >= mn:
        p2 += mx - mn + 1

p2 = 2 ** 32 - p2
print(f'Part 2: {p2}')
