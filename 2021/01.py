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
    for line in f:
        inp.append(int(line.rstrip()))

vals = []
prev = None
for val in inp:
    if prev is not None:
        if val > prev:
            p1 += 1
    prev = val
    vals.append(val)
print(f'Part 1: {p1}')

windows = []
for x in range(len(vals)-2):
    window = 0
    for y in range(3):
        window += vals[x+y]
    windows.append(window)
for x in range(1, len(windows)):
    if windows[x] > windows[x-1]:
        p2 += 1
print(f'Part 2: {p2}')
