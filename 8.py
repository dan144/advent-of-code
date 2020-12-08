#!/usr/bin/env python3

import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append([line.split()[0], int(line.split()[1]), False])

def run(cmd):
    acc = 0
    ip = 0
    try:
        while True:
            if cmd[ip][2]:
                break
            ins = cmd[ip]
            ins[2] = True
            if ins[0] == 'nop':
                ip += 1
            elif ins[0] == 'acc':
                acc += ins[1]
                ip += 1
            elif ins[0] == 'jmp':
                ip += ins[1]
    except:
        return acc, True
    return acc, False

p1, _ = run(deepcopy(inp))
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
