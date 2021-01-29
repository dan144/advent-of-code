#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

with open(input_file) as f:
    cmds = utils.load_split_lines(f)

def run(debug):
    global p1
    ip = 0
    regs = {k: 0 for k in 'abcdefgh'}
    regs['a'] = 1 if debug else 0
    while ip in range(len(cmds)):
        if debug and ip >= 9:
            # short circuit execution, necessary registers set
            return regs
        cmd = cmds[ip]
        op = cmd[0]
        if op == 'set':
            x = cmd[1]
            try:
                y = int(cmd[2])
            except ValueError:
                y = regs[cmd[2]]
            regs[x] = y
        elif op == 'sub':
            x = cmd[1]
            try:
                y = int(cmd[2])
            except:
                y = regs[cmd[2]]
            regs[x] = regs.get(x, 0) - y
        elif op == 'mul':
            p1 += 1
            x = cmd[1]
            try:
                y = int(cmd[2])
            except ValueError:
                y = regs[cmd[2]]
            regs[x] = regs.get(x, 0) * y
        elif op == 'jnz':
            try:
                x = int(cmd[1])
            except:
                x = regs.get(cmd[1], 0)
            if x != 0:
                try:
                    ip += int(cmd[2])
                except:
                    ip += regs[cmd[2]]
                continue
        ip += 1
    return regs
    
run(False)
print(f'Part 1: {p1}')

regs = run(True)
# count number of composite numbers between regs b and c, inclusive
p2 = 0
for n in range(regs['b'], regs['c'] + 1, 17):
    p2 += 0 if utils.is_prime(n) else 1
print(f'Part 2: {p2}')
