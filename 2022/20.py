#!/usr/bin/env python3

import sys

import utils

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    inp = utils.load_num_lines(f) # one int per line

# Part 1

nums = []
for x in inp:
    nums.append({'value': x, 'moved': False})

while True:
    idx = 0
    for x in nums:
        if x['moved'] is False:
            break
        idx += 1
    else:
        break
    idx += x['value']
    nums.remove(x)
    idx = idx % len(nums)
    while idx < 0:
        idx += len(nums)
    nums.insert(idx, x)
    x['moved'] = True
    if test:
        print(f"{x['value']} moves between {nums[idx-1]['value']} and {nums[idx+1]['value']}")
        for x in nums:
            print(x['value'], end=' ')
        print()
        print()

vals = []
for i, x in enumerate(nums):
    v = x['value']
    if v == 0:
        idx = i
    vals.append(v)

vals = vals[idx:] + vals[:idx]
l = len(vals)
print(vals)

print(vals[1000 % l], vals[2000 % l], vals[3000 % l])
p1 = vals[1000 % l] + vals[2000 % l] + vals[3000 % l]
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
