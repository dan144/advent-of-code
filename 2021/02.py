#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    inp = utils.load_split_lines(f) # asdf asdf asdf ...

# x is forward, y is depth

# Part 1
x, y = 0, 0
for direc, m in inp:
    if direc == 'forward':
        x += int(m)
    elif direc == 'down':
        y += int(m)
    else:
        y -= int(m)
p1 = x * y
print(f'Part 1: {p1}')

# Part 2
x, y, aim = 0, 0, 0
for direc, m in inp:
    if direc == 'forward':
        x += int(m)
        y += aim * int(m)
    elif direc == 'down':
        aim += int(m)
    else:
        aim -= int(m)
p2 = x * y
print(f'Part 2: {p2}')
