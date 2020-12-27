#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    nums = list(map(int, [n for n in f.readline().rstrip('\n').split(',')]))

spoken = {}
for i, n in enumerate(nums):
    spoken[n] = spoken.get(n, [])
    spoken[n].append(i)

for i in range(len(nums), 30000000):
    arr = spoken.get(n, [])
    n = abs(arr[-1] - arr[-2]) if len(arr) > 1 else 0

    if n in spoken:
        spoken[n].append(i)
    else:
        spoken[n] = [i]

    if i == 2019:
        p1 = n
        print(f'Part 1: {p1}')

p2 = n
print(f'Part 2: {p2}')
