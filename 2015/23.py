#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

cmds = []
with open(input_file) as f:
    for line in f:
        cmds.append(line.rstrip().split())

def run(cmds, regs):
    ip = 0
    while 0 <= ip < len(cmds):
        cmd = cmds[ip]
        if cmd[0] == 'hlf':
            regs[cmd[1]] //= 2
        elif cmd[0] == 'tpl':
            regs[cmd[1]] *= 3
        elif cmd[0] == 'inc':
            regs[cmd[1]] += 1
        elif cmd[0] == 'jmp':
            ip += int(cmd[1])
            continue
        elif cmd[0] == 'jie':
            if regs[cmd[1].rstrip(',')] % 2 == 0:
                ip += int(cmd[2])
                continue
        elif cmd[0] == 'jio':
            if regs[cmd[1].rstrip(',')] == 1:
                ip += int(cmd[2])
                continue
        ip += 1
    return regs


regs = {'a': 0, 'b': 0}
run(cmds, regs)
p1 = regs['b']
print(f'Part 1: {p1}')


regs = {'a': 1, 'b': 0}
run(cmds, regs)
p2 = regs['b']
print(f'Part 2: {p2}')
