#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file, 'r') as f:
    ans = set()
    for line in f:
        if line == '\n':
            inp.append(ans)
            ans = set()
        else:
            ans.update(list(line[:-1]))
inp.append(ans)

for group in inp:
    p1 += len(group)

print(f'Part 1: {p1}')

with open(input_file, 'r') as f:
    ans = set()
    first = True
    for line in f:
        if line == '\n':
            p2 += len(ans)
            ans = set()
            first = True
        else:
            if first is True:
                ans = set(list(line[:-1]))
                first = False
            else:
                ans = ans.intersection(set(list(line[:-1])))
p2 += len(ans)

print(f'Part 2: {p2}')
