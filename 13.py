#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

buses = []
first = None
with open(input_file) as f:
    first = int(f.readline())
    for b in f.readline().rstrip('\n').split(','):
        try:
            b = int(b)
        except:
            pass
        buses.append(b)

low = (10000, 0)
inc = None
m = 1
for bus in buses:
    try:
        b = int(bus)
        t = b
        while t < first:
            t += b
        diff = t - first
        if diff < low[0]:
            low = (diff, b)
    except:
        pass

p1 = low[0] * low[1]
print(f'Part 1: {p1}')

p2 = 0 if test else 100000000000000
inc = 1
for b in range(len(buses)):
    if buses[b] == 'x':
        continue
    while (p2 + b) % buses[b] != 0:
        p2 += inc
    inc *= buses[b]
print(f'Part 2: {p2}')
