#!/usr/bin/env python3

import sys

from copy import deepcopy

from computer import parse, run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

cmds = parse(input_file)

p1, _ = run(cmds)
print(f'Part 1: {p1}')

for i in range(len(cmds)):
    if cmds[i][0] == 'nop':
        continue
    cmd = deepcopy(cmds)
    cmd[i][0] = 'jmp' if cmd[i][0] == 'nop' else 'nop'
    p2, done = run(cmd)
    if done:
        print(f'Swapped command {i} to be {cmd[i][0]}')
        break

print(f'Part 2: {p2}')
