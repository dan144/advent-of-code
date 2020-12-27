#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(int(line))

n_preamble = 5 if test else 25
preamble = inp[:n_preamble]

for n in inp[n_preamble:]:
    valid = False
    for a in range(n_preamble):
        for b in range(n_preamble):
            if preamble[a] == preamble[b]:
                continue
            if preamble[a] + preamble[b] == n:
                valid = True
                break
    else:
        preamble.pop(0)
        preamble.append(n)
    if not valid:
        p1 = n
        break
print(f'Part 1: {p1}')

for start in range(len(inp)):
    total = 0
    i = 0
    while total < p1:
        total += inp[start + i]
        i += 1
    if total == p1:
        p2 = min(inp[start:start+i]) + max(inp[start:start+i])
        break

print(f'Part 2: {p2}')
