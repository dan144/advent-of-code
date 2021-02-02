#!/usr/bin/env python3

import re
import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    inp = f.readline().rstrip()

r = re.compile('[A-Z]|\(\d+x\d+\)')

def dig(markers, recurse):
    total = 0
    while markers:
        if '(' in markers[0]:
            c, n = map(int, re.findall(r'\d+', markers[0]))
            new = []
            while len(''.join(new)) < c:
                new.append(markers.pop(1))

            if recurse:
                total += n * dig(new, recurse)
            else:
                total += n * c
        else:
            total += len(markers[0])
        markers.pop(0)
    return total

markers = r.findall(inp)

p1 = dig(copy(markers), False)
print(f'Part 1: {p1}')

p2 = dig(copy(markers), True)
print(f'Part 2: {p2}')
