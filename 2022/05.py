#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = ''
p2 = ''

def run(part):
    if part == 1:
        order = 1
    else:
        order = -1

    towers = []
    moving = False
    with open(input_file) as f:
        for line in f:
            if moving:
                x, f, t = map(int, re.findall(r'[0-9]+', line))
                n = []
                for i in range(x):
                    m = towers[f - 1].pop()
                    n.append(m)
                towers[t - 1].extend(n[::order])
            else:
                if line == '\n':
                    moving = True
                else:
                    for x in range(len(line) // 4 + 1):
                        box = line[4 * x:4 * (x + 1)]
                        if box.startswith('['):
                            while len(towers) <= x:
                                towers.append([])
                            towers[x].insert(0, box[1])
    return towers

towers = run(1)
for tower in towers:
    p1 += tower[-1]
print(f'Part 1: {p1}')

towers = run(2)
for tower in towers:
    p2 += tower[-1]
print(f'Part 2: {p2}')
