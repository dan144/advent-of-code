#!/usr/bin/env python3

import sys

import utils
# display_grid((y, x) grid) - display values in 2D map grid

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

# Part 1

needed = [20, 60, 100, 140, 180, 220]
cycle = 0
X = 1
display = {}
for cmd in inp:
    cmd = cmd.split()

    pixel = (cycle // 40, cycle % 40)
    display[pixel] = '#' if pixel[1] in {X - 1, X, X + 1} else '.'
    cycle += 1
    if cycle in needed:
        p1 += cycle * X

    if cmd[0] == 'noop':
        continue

    # otherwise is an addx command
    pixel = (cycle // 40, cycle % 40)
    display[pixel] = '#' if pixel[1] in {X - 1, X, X + 1} else '.'
    cycle += 1
    if cycle in needed:
        p1 += cycle * X

    X += int(cmd[1])

print(f'Part 1: {p1}')

# Part 2
print(f'Part 2')
utils.display_grid(display)
