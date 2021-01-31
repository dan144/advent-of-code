#!/usr/bin/env python3

import re
import sys

from blist import blist

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    num = int(f.readline().rstrip())

elves = list(range(num))
while len(elves) != 1:
    print(f'\r{len(elves)}', end=' ')
    remove = set()
    for i in range(0, len(elves), 2):
        try:
            remove.add(elves[i+1])
        except IndexError:
            remove.add(elves[0])
    elves = list(sorted(set(elves) - remove))

p1 = elves.pop() + 1
print(f'\rPart 1: {p1}')

elves = blist(range(1, num + 1))
while len(elves) != 1:
    if len(elves) % 1000 == 0:
        print(f'\r{len(elves)}', end=' ')

    n_other = len(elves) // 2
    elves.pop(n_other)
    elves = elves[1:] + [elves[0]]

p2 = elves.pop()
print(f'\rPart 2: {p2}')
