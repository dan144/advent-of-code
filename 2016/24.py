#!/usr/bin/env python3

import itertools
import re
import sys

from copy import deepcopy

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = float('inf')
p2 = float('inf')

inp = []
with open(input_file) as f:
    grid = utils.load_grid(f)

nums = set()
for loc, v in deepcopy(grid).items():
    if v not in '.#':
        nums.add(loc)
    if v == '0':
        start = loc
    grid[loc] = v != '#'

dists = {}
for l1 in sorted(nums):
    for l2 in sorted(nums):
        if l1 == l2:
            continue
        if (l1, l2) in dists.keys():
            continue
        dist = utils.find_dist(grid, 0, {l1}, l2)
        dists[l1, l2] = dist

nums.remove(start)
for path in itertools.permutations(nums):
    dist = 0
    go_from = start
    for go_to in path:
        dist += dists[tuple(sorted((go_from, go_to)))]
        go_from = go_to
    p1 = min(p1, dist)
    p2 = min(p2, dist + dists[tuple(sorted((go_from, start)))])

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
