#!/usr/bin/env python3

import itertools
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

def comp_qe(packages):
    t = 1
    for p in packages:
        t *= p
    return t

with open(input_file) as f:
    nums = sorted(utils.load_num_lines(f), reverse=True)
t_weight = sum(nums)

def run(n_groups):
    ans = float('inf')
    g_weight = t_weight // n_groups
    n = 2
    while ans == float('inf'):
        for packages in itertools.combinations(nums, n):
            if sum(packages) == g_weight:
                qe = comp_qe(packages)
                ans = min(ans, qe)
        n += 1
    return ans

p1 = run(3)
print(f'Part 1: {p1}')

p2 = run(4)
print(f'Part 2: {p2}')
