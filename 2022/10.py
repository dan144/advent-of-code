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

cycles = [1]
cycle = 0
X = 1
display = {}
for cmd in inp:
    pixel = (cycle // 40, cycle % 40)
    cmd = cmd.split()
    if cmd[0] == 'noop':
        cycles.append(X)
        display[pixel] = '#' if pixel[1] in {X - 1, X, X + 1} else '.'
        cycle += 1
    elif cmd[0] == 'addx':
        cycles.append(X)
        display[pixel] = '#' if pixel[1] in {X - 1, X, X + 1} else '.'
        cycle += 1
        cycles.append(X)
        pixel = (cycle // 40, cycle % 40)
        display[pixel] = '#' if pixel[1] in {X - 1, X, X + 1} else '.'
        cycle += 1
        X += int(cmd[1])

for x in [20, 60, 100, 140, 180, 220]:
    p1 += cycles[x] * x
print(f'Part 1: {p1}')

# Part 2
print(f'Part 2')
utils.display_grid(display)
