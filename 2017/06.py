#!/usr/bin/env python3

import sys

from copy import copy

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    nums = utils.load_one_line_of_nums(f)

seen = {}
allocations = copy(nums)
count = 0
while tuple(allocations) not in seen:
    seen[tuple(allocations)] = count
    count += 1
    most = 0
    for i, num in enumerate(allocations):
        if num > allocations[most]:
            most = i

    redist = allocations[most]
    allocations[most] = 0
    for n in range(redist):
        allocations[(most + n + 1) % len(allocations)] += 1

p1 = len(seen)
p2 = count - seen[tuple(allocations)]
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
