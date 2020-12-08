#!/usr/bin/env python3

import sys

from copy import deepcopy

from computer import run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        ins, off = line.split()
        inp.append([ins, int(off), False])

p1, _ = run(inp)
print(f'Part 1: {p1}')

for i in range(len(inp)):
    if inp[i][0] == 'nop':
        continue
    cmd = deepcopy(inp)
    cmd[i][0] = 'jmp' if cmd[i][0] == 'nop' else 'nop'
    p2, done = run(cmd)
    if done:
        break

print(f'Part 2: {p2}')
