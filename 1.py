#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file, 'r') as f:
    for line in f:
        inp.append(int(line))

n = len(inp)

for a in range(n):
    for b in range(n):
        if a != b and inp[a] + inp[b] == 2020:
            p1 = inp[a] * inp[b]
print(f'Part 1: {p1}')

for a in range(n):
    for b in range(n):
        for c in range(n):
            if a != b and b != c and c != a and inp[a] + inp[b] + inp[c] == 2020:
                p2 = inp[a] * inp[b] * inp[c]
print(f'Part 2: {p2}')
