#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    for line in f:
        # for each x-y in line, create a set of that range of numbers
        a, b = map(lambda x: set(range(int(x[0]), int(x[1])+1)), re.findall(r'([0-9]+)-([0-9]+)', line))
        shared = a & b

        if shared == b or shared == a: # shared numbers equal one of the whole sets
            p1 += 1
        if shared:
            p2 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
