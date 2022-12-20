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

def run(part):
    nums = []
    for i, x in enumerate(inp):
        x *= 811589153 if part == 2 else 1
        nums.append({'value': x, 'idx': i})

    for j in range(10 if part == 2 else 1):
        if test is False:
            print(f'\rMix: {j+1}', end='')

        for which in range(len(inp)):
            for idx, x in enumerate(nums):
                if x['idx'] == which:
                    break

            idx += x['value']
            nums.remove(x)

            idx = idx % len(nums)
            while idx < 0:
                idx += len(nums)

            nums.insert(idx, x)

            #if test:
            #    print(f"{x['value']} moves between {nums[idx-1]['value']} and {nums[idx+1]['value']}")
            #    for x in nums:
            #        print(x['value'], end=' ')
            #    print()
            #    print()

    vals = []
    for i, x in enumerate(nums):
        v = x['value']
        if v == 0:
            idx = i
        vals.append(v)

    vals = vals[idx:] + vals[:idx]
    l = len(vals)

    #if test:
    #    print(vals[1000 % l], vals[2000 % l], vals[3000 % l])
    if test is False:
        print()
    return vals[1000 % l] + vals[2000 % l] + vals[3000 % l]

p1 = run(1)
print(f'Part 1: {p1}')
p2 = run(2)
print(f'Part 2: {p2}')
