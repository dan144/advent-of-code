#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = ''
p2 = ''

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.rstrip())

most = []
for i in range(len(inp[0])):
    most.append({})

for word in inp:
    for i, c in enumerate(word):
        if c not in most[i]:
            most[i][c] = 0
        most[i][c] += 1

for i in range(len(inp[0])):
    p1 += sorted(most[i].items(), key=lambda x: x[1], reverse=True)[0][0]

print(f'Part 1: {p1}')

for i in range(len(inp[0])):
    p2 += sorted(most[i].items(), key=lambda x: x[1])[0][0]

print(f'Part 2: {p2}')
