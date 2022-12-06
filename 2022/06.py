#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    for line in f:
        stream = line.strip()
stream = stream + stream # since it overflows

def run(num_chars):
    for i in range(num_chars, len(stream) - num_chars):
        chars = set(stream[i-num_chars:i])
        if len(chars) == num_chars:
            return i
    else:
        assert False

# Part 1
p1 = run(4)
print(f'Part 1: {p1}')

# Part 2
p2 = run(14)
print(f'Part 2: {p2}')
