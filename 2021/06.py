#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    inp = utils.load_comma_sep_nums(f) # 1,2,3,...

timer = {}
for v in inp:
    timer[v] = timer.get(v, 0) + 1

for day in range(256):
    new = timer.get(0, 0)
    for l in range(8):
        timer[l] = timer.get(l+1, 0)
    timer[8] = new
    timer[6] += new
    #print(sorted(timer.items(), key=lambda x: x[0]))
    if day == 79:
        p1 = sum(timer.values())
p2 = sum(timer.values())

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
