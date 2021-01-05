#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file, 'r') as f:
    ans1 = set()
    ans2 = None
    for line in f:
        if line == '\n':
            p1 += len(ans1)
            p2 += len(ans2)
            ans1 = set()
            ans2 = None
        else:
            ans1.update(list(line[:-1]))
            if ans2 is None:
                ans2 = set(list(line[:-1]))
            else:
                ans2 = ans2.intersection(set(list(line[:-1])))
p1 += len(ans1)
p2 += len(ans2)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
