#!/usr/bin/env python3

import itertools
import re
import sys

import utils

from blist import blist

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    steps = int(f.readline().rstrip())

pos = 0
nums = blist([0])
for i in range(1, 2017 + 1):
    pos = (pos + steps) % len(nums) + 1
    nums.insert(pos, i)

idx = nums.index(2017)
p1 = nums[(idx + 1) % len(nums)]
print(f'Part 1: {p1}')

for i in range(i + 1, 50000000 + 1):
    if i % 100000 == 0:
        print(f'\r{i}', end='')
    pos = (pos + steps) % len(nums) + 1
    nums.insert(pos, i)

idx = nums.index(0)
p2 = nums[(idx + 1) % len(nums)]
print(f'\nPart 2: {p2}')
