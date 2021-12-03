#!/usr/bin/env python3

from copy import copy
import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges: min_x, min_y, max_x, max_y
# display_grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 1

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

# Part 1
z, o = [0] * len(inp[0]), [0] * len(inp[0])
for num in inp:
    for i, bit in enumerate(num):
        if bit == '0':
            z[i] += 1
        else:
            o[i] += 1

g = ''
e = ''
for i in range(len(z)):
    if z[i] > o[i]:
        g += '0'
        e += '1'
    else:
        g += '1'
        e += '0'

g = int(g, 2)
e = int(e, 2)
p1 = g * e
print(f'Part 1: {p1}')

# Part 2
for t in range(2):
    nums = copy(inp)
    i = 0
    while len(nums) > 1:
        z, o = 0, 0
        for num in nums:
            if num[i] == '0':
                z += 1
            else:
                o += 1
        if t == 0: # oxygen, most common
            if o >= z:
                d = '1'
            else:
                d = '0'
        else:
            if o >= z:
                d = '0'
            else:
                d = '1'
        nums = list(filter(lambda x: x[i] == d, nums))
        i += 1
    p2 *= int(nums.pop(), 2)

print(f'Part 2: {p2}')
