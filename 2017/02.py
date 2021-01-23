#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(list(map(int, line.rstrip().split())))

for line in inp:
    p1 += max(line) - min(line)

print(f'Part 1: {p1}')

for line in inp:
    for i, a in enumerate(line):
        for j, b in enumerate(line):
            if i == j or b > a:
                continue
            if a % b == 0:
                p2 += a // b

print(f'Part 2: {p2}')
