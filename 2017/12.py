#!/usr/bin/env python3

import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

programs = {}
with open(input_file) as f:
    for line in f:
        p, s = line.rstrip().split(' <-> ')
        s = s.split(', ')
        programs[p] = s

def find_group(start):
    add_from = {start}
    added = set()
    while add_from:
        for p in copy(add_from):
            s = programs[p]
            added.add(p)
            add_from.update(s)
        add_from = add_from - added
    return added

group = find_group('0')
p1 = len(group)
print(f'Part 1: {p1}')

p2 = 0
while programs:
    p2 += 1
    group = find_group(list(programs.keys())[0])
    for p in group:
        programs.pop(p)

print(f'Part 2: {p2}')
