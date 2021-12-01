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
        inp.append(line.rstrip())

# Part 1

print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
