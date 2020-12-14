#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

earliest = None
with open(input_file) as f:
    earliest = int(f.readline())
    inp = f.readline().rstrip('\n').split(',')
    buses = {i: int(inp[i]) for i in range(len(inp)) if inp[i] != 'x'}

low = (float('inf'), 0)
for bus in buses.values():
    t = bus
    while t < earliest:
        t += bus
    diff = t - earliest
    low = (diff, bus) if diff < low[0] else low

p1 = low[0] * low[1]
print(f'Part 1: {p1}')

p2 = 0 if test else 100000000000000
inc = 1
for b, bus in buses.items():
    while (p2 + b) % bus != 0:
        p2 += inc
    inc *= bus
print(f'Part 2: {p2}')
