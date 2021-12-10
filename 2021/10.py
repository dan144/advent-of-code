#!/usr/bin/env python3

import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges: min_x, min_y, max_x, max_y
# display_grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime
# adjs - set of dx,dy values for LRUD adjacencies
# diags - set of dx,dy values for diagonals
# all_dirs set of dx,dy values for all 8 surrounding values

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

# Part 1
incomplete = []
corrupted = []
scores = []
for line in inp:
    stack = []
    corrupt = False
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif c in ')]}>':
            check = stack.pop(-1)
            if check + c in {'()', '[]', '{}', '<>'}:
                continue
            else:
                score = {
                    ')': 3,
                    ']': 57,
                    '}': 1197,
                    '>': 25137,
                }
                p1 += score[c]
                corrupt = True
    if corrupt:
        corrupted.append(line)
    else:
        incomplete.append(line)
        score = 0
        for c in stack[::-1]:
            score *= 5
            score += {
                '(': 1,
                '[': 2,
                '{': 3,
                '<': 4,
            }[c]
        scores.append(score)

print(f'Part 1: {p1}')

# Part 2
l = len(scores) // 2
p2 = sorted(scores)[l]
print(f'Part 2: {p2}')
