#!/usr/bin/env python3

import sys
from itertools import combinations

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = {0}
with open(input_file) as f:
    for line in f:
        inp.add(int(line))
inp.add(max(inp)+3)
jolts = sorted(inp)

chunks = []
chunk = []
ones = 0
threes = 0
for j in range(len(jolts)-1):
    if jolts[j+1] == jolts[j] + 1:
        ones += 1
    elif jolts[j+1] == jolts[j] + 3:
        threes += 1

    chunk.append(jolts[j])
    if jolts[j] + 3 == jolts[j+1]:
        # chunks are grouped by values with a difference < 3
        chunks.append(chunk)
        chunk = []

p1 = ones * threes
print(f'Part 1: {p1}')

def is_legal(path):
    for j in range(len(path)-1):
        if path[j] + 3 < path[j+1]:
            return False
    return True

p2 = 1
for chunk in chunks:
    # chunks with len <= 2 have no subpaths
    if len(chunk) <= 2:
        continue

    multiples = 0
    mn = chunk.pop(0)
    mx = chunk.pop(-1)

    # check all combinations of interior numbers and count valid paths from min to max
    for l in range(len(chunk)+1):
        for c in combinations(chunk, l):
            multiples += is_legal((mn,) + c + (mx,))
    p2 *= multiples

print(f'Part 2: {p2}')
