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

ins = {}
polymer = ''
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if not polymer:
            polymer = line
        else:
            o, n = line.split(' -> ')
            ins[o] = n

def count():
    occs = {}
    for x, c in sp.items():
        for a in x:
            if a not in occs:
                occs[a] = 0
            occs[a] += c

    occs[polymer[0]] += 1
    occs[polymer[-1]] += 1
    for k in occs.keys():
        occs[k] //= 2
    
    v = sorted(occs.values())
    return v[-1] - v[0]

sp = {}
for i in range(len(polymer)-1):
    a, b = polymer[i], polymer[i+1]
    if a+b not in sp:
        sp[a+b] = 0
    sp[a+b] += 1

for step in range(40):
    new = {}
    for x, c in sp.items():
        a, b = x
        n = ins[x]
        f = a + n
        s = n + b
        if f not in new:
            new[f] = 0
        new[f] += c
        if s not in new:
            new[s] = 0
        new[s] += c
    sp = new

    if step == 9:
        p1 = count()

p2 = count()
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
