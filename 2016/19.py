#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    num = int(f.readline().rstrip())

elves = list(range(num))
while len(elves) != 1:
    print(len(elves))
    remove = set()
    for i in range(0, len(elves), 2):
        try:
            remove.add(elves[i+1])
        except IndexError:
            remove.add(elves[0])
    elves = list(sorted(set(elves) - remove))

p1 = elves.pop() + 1
print(f'Part 1: {p1}')

elves = {x + 1 for x in range(num)}
i = 0
while len(elves) != 1:
    if len(elves) % 1000 == 0:
        print(len(elves))

    n_other = (len(elves) - 1) / 2
    n_other = int(n_other) + (1 if n_other % 1 != 0 else 0)
    n_other = (n_other + i) % len(elves)

    other = sorted(elves)[n_other]
    elves.remove(other)

    i += 1
    if i > len(elves):
        i = 0

p2 = elves.pop()
print(f'Part 2: {p2}')
