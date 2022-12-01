#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

cals = [0]
with open(input_file) as f:
    for line in f:
        if cal := line.strip():
            cals[-1] += int(cal)
        else:
            cals.append(0)

p1 = max(cals)
print(f'Part 1: {p1}')

p2 = sum(sorted(cals, reverse=True)[:3])
print(f'Part 2: {p2}')
