#!/usr/bin/env python3

import re
import sys

from assembunny import run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

cmds = []
with open(input_file) as f:
    for line in f:
        cmds.append(line.rstrip().split())

regs = {x: 0 for x in 'abcd'}
run(cmds, regs)
p1 = regs['a']
print(f'Part 1: {p1}')

regs = {x: 0 for x in 'abcd'}
regs['c'] = 1
run(cmds, regs)
p2 = regs['a']
print(f'Part 2: {p2}')
