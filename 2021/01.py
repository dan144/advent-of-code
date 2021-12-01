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
    inp = utils.load_num_lines(f)

for x in range(len(inp)):
    if inp[x] > inp[x-1]:
        p1 += 1
print(f'Part 1: {p1}')

windows = []
for x in range(len(inp)-2):
    window = 0
    for y in range(3):
        window += inp[x+y]
    windows.append(window)

for x in range(1, len(windows)):
    if windows[x] > windows[x-1]:
        p2 += 1
print(f'Part 2: {p2}')
