#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    inp = f.readline().rstrip().split(',')

programs = list('abcde') if test else list('abcdefghijklmnop')

def dance():
    for cmd in inp:
        if cmd.startswith('s'):
            x = int(cmd[1:])
            for _ in range(x):
                e = programs.pop(-1)
                programs.insert(0, e)
        elif cmd.startswith('p'):
            a, b = cmd[1], cmd[3]
            ai = programs.index(a)
            bi = programs.index(b)
            programs[ai], programs[bi] = programs[bi], programs[ai]
        elif cmd.startswith('x'):
            a, b = list(map(int, re.findall(r'\d+', cmd)))
            programs[a], programs[b] = programs[b], programs[a]

dance()
p1 = ''.join(programs)
print(f'Part 1: {p1}')

seen = {}
n = 1
while True:
    a = ''.join(programs)
    if a in seen:
        seen[a].append(n)
        if len(seen[a]) == 3:
            # found 3 evenly spaced occurrences in a cycle
            if seen[a][2] - seen[a][1] == seen[a][1] - seen[a][0]:
                break
    else:
        seen[a] = [n]
    dance()
    n += 1

cycle = seen[a][2] - seen[a][1]
reduced = 1000000000 % cycle

# find the pattern that happened at the first iteration in the cycle
for k, v in seen.items():
    if v[0] == reduced:
        break
p2 = ''.join(k)
print(f'Part 2: {p2}')
