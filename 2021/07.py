#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = float('inf')
p2 = float('inf')

inp = []
with open(input_file) as f:
    inp = utils.load_comma_sep_nums(f) # 1,2,3,...

# Part 1
mn = min(inp)
mx = max(inp)

for x in range(mn, mx+1):
    cost = 0
    for crab in inp:
        cost += abs(crab - x)
    p1 = min(cost, p1)
print(f'Part 1: {p1}')

# Part 2
for x in range(mn, mx+1):
    cost = 0
    for crab in inp:
        n = abs(crab - x)
        cost += n * (n+1) // 2 # triangular number formula, closed form of summing 1,2,..,n
    p2 = min(p2, cost)
print(f'Part 2: {p2}')
