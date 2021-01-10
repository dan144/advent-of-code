#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = float('inf')
p2 = float('inf')

def comp_qe(packages):
    t = 1
    for p in packages:
        t *= p
    return t

with open(input_file) as f:
    nums = sorted(utils.load_num_lines(f), reverse=True)

t_weight = sum(nums)
g_weight = t_weight // 3

n = 2
while p1 == float('inf'):
    for packages in itertools.combinations(nums, n):
        if sum(packages) == g_weight:
            qe = comp_qe(packages)
            p1 = min(p1, qe)
    n += 1

print(f'Part 1: {p1}')

g_weight = t_weight // 4
n = 2
while p2 == float('inf'):
    for packages in itertools.combinations(nums, n):
        if sum(packages) == g_weight:
            qe = comp_qe(packages)
            p2 = min(p2, qe)
    n += 1

print(f'Part 2: {p2}')
