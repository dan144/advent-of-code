#!/usr/bin/env python3

import sys

from copy import copy

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    o_nums = utils.load_num_lines(f)

nums = copy(o_nums)

ip = 0
while ip in range(len(nums)):
    nums[ip] += 1
    ip += nums[ip] - 1
    p1 += 1

print(f'Part 1: {p1}')

nums = copy(o_nums)
ip = 0
while ip in range(len(nums)):
    offset = nums[ip]
    if offset >= 3:
        nums[ip] -= 1
    else:
        nums[ip] += 1
    ip += offset
    p2 += 1

print(f'Part 2: {p2}')
