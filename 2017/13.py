#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(list(map(int, re.findall(r'\d+', line))))

def run(start):
    pos = []
    sev = 0
    for _ in range(len(inp)):
        pos.append([0, 1])
    for t in range(inp[-1][0] + 1 + start):
        for i, (d, r) in enumerate(inp):
            if t - start == d and pos[i][0] == 0:
                sev += d * r
            pos[i][0] += pos[i][1]
            if pos[i][0] in {0, r - 1}:
                pos[i][1] *= -1
    return sev

p1 = run(0)
print(f'Part 1: {p1}')

def caught_at(start):
    for d, r in inp:
        if (start + d) % ((r - 1) * 2) == 0:
            return True
    return False

sev = 1
p2 = 0
while caught_at(p2):
    p2 += 1
print(f'Part 2: {p2}')
