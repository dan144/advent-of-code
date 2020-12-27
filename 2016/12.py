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
    while ip < len(cmds):
        cmd = cmds[ip]
        opcode = cmd[0]
        if opcode == 'cpy':
            try:
                regs[cmd[2]] = int(cmd[1])
            except:
                regs[cmd[2]] = regs[cmd[1]]
        elif opcode == 'inc':
            regs[cmd[1]] += 1
        elif opcode == 'dec':
            regs[cmd[1]] -= 1
        elif opcode == 'jnz':
            try:
                x = regs[cmd[1]]
            except:
                x = int(cmd[1])
            if x != 0:
                ip += int(cmd[2])
                continue
        ip += 1

regs = {x: 0 for x in 'abcd'}
run(cmds, regs)
p1 = regs['a']
print(f'Part 1: {p1}')

regs = {x: 0 for x in 'abcd'}
regs['c'] = 1
run(cmds, regs)
p2 = regs['a']
print(f'Part 2: {p2}')
