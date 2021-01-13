#!/usr/bin/env python3

import sys

from copy import deepcopy

from assembunny import run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

cmds = []
mul_by = []
with open(input_file) as f:
    for line in f:
        line = line.rstrip().split()
        try:
            if int(line[1]) > 10:
                mul_by.append(int(line[1]))
        except ValueError:
            pass
        cmds.append(line)

def factorial(n):
    return n if n < 2 else factorial(n - 1) * n

p1 = 0
while True:
    regs = {x: 0 for x in 'abcd'}
    regs['a'] = p1
    if run(deepcopy(cmds), regs):
        break
    p1 += 1

print(f'Part 1: {p1}')
