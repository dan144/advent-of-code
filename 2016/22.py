#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

nodes = {}
with open(input_file) as f:
    for line in f:
        try:
            d = re.findall(r'\d+', line)
            x = int(d.pop(0))
            y = int(d.pop(0))
            nodes[x, y] = list(map(int, d))
        except IndexError:
            pass

for l1 in nodes.keys():
    for l2 in nodes.keys():
        nA = nodes[l1]
        nB = nodes[l2]
        if nA[1] != 0 and l1 != l2 and nA[1] <= nB[2]:
            p1 += 1

print(f'Part 1: {p1}')


print(f'Part 2: {p2}')
