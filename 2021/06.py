#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    inp = utils.load_comma_sep_nums(f) # 1,2,3,...

nums = {}
for v in inp:
    nums[v] = nums.get(v, 0) + 1

for day in range(256):
    new = nums.get(0, 0)
    for l in range(8):
        nums[l] = nums.get(l+1, 0)
    nums[8] = new
    nums[6] += new
    #print(sorted(nums.items(), key=lambda x: x[0]))
    if day == 79:
        p1 = sum(nums.values())
p2 = sum(nums.values())

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
