#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 0

cmds = []
with open(input_file) as f:
    for line in f:
        line = line.rstrip().split()
        line[2] = int(line[2])
        cmds.append(line)

regs = {}
ip = 0
while ip in range(len(cmds)):
    cmd = cmds[ip]
    r = regs.get(cmd[4], 0)
    op = cmd[5]
    if eval(str(r) + op + cmd[6]):
        s = regs.get(cmd[0], 0)
        regs[cmd[0]] = s + cmd[2] * (1 if cmd[1] == 'inc' else -1)
        p2 = max(p2, regs[cmd[0]])
    ip += 1

p1 = max(regs.values())
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
