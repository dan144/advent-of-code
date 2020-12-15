#!/usr/bin/env python3

import re
import sys

from computer import parse, run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    nums = list(map(int, [n for n in f.readline().rstrip('\n').split(',')]))

spoken = {}
for i in range(30000000):
    if nums:
        n = nums.pop(0)
    else:
        arr = spoken.get(n, [])
        if len(arr) <= 1:
            n = 0
        else:
            n = abs(spoken[n][-1] - spoken[n][-2])
    if n in spoken:
        spoken[n].append(i)
    else:
        spoken[n] = [i]
        spoken[n] = spoken[n][:-2]
    if i == 2020:
        p1 = n

print(f'Part 1: {p1}')
p2 = n
print(f'Part 2: {p2}')
