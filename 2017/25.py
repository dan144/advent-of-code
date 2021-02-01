#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

current = None
actions = {}
start = False
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if current is None:
            current = line.rstrip('.').split()[-1]
        elif line:
            if not start:
                start = True
                steps = int(line.split()[-2])
            else:
                if line.startswith('In'):
                    state = line.rstrip(':').split()[-1]
                    actions[state] = {}
                elif line.startswith('If'):
                    value = line.rstrip(':').split()[-1]
                    actions[state][value] = []
                elif line.startswith('-'):
                    act = line.rstrip('.').split()[-1]
                    actions[state][value].append(act)
                else:
                    assert False

checksum = {}
spot = 0
print(f'{steps} steps to run')
for step in range(steps):
    if step % 1000 == 0:
        print(f'\r{step}', end='')
    value = str(checksum.get(spot, 0))
    act = actions[current][value]
    checksum[spot] = int(act[0])
    spot += 1 if act[1] == 'right' else -1
    current = act[2]

p1 = sum(checksum.values())
print(f'\nPart 1: {p1}')
