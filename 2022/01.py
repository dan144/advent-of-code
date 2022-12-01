#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())
    inp.append('') # to flush

# Part 1

subtotal = 0
cals = []
for cal in inp:
    if cal == '':
        cals.append(subtotal)
        p1 = max(subtotal, p1)
        subtotal = 0
    else:
        subtotal += int(cal)

print(f'Part 1: {p1}')

cals = sorted(cals, reverse=True)
p2 = sum(cals[:3])
print(f'Part 2: {p2}')
