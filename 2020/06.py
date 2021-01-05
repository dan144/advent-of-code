#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

ans1 = set()
ans2 = None
with open(input_file, 'r') as f:
    for line in f:
        line = line.rstrip()
        if line:
            ans1.update(list(line))
            ans2 = set(list(line)) if ans2 is None else ans2.intersection(set(list(line)))
        else:
            p1 += len(ans1)
            p2 += len(ans2)
            ans1 = set()
            ans2 = None
p1 += len(ans1)
p2 += len(ans2)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
