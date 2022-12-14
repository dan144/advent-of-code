#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

lists = []
with open(input_file) as f:
    s = []
    for line in f:
        line = line.strip()
        if line:
            s.append(eval(line))
        else:
            lists.append(s)
            s = []
lists.append(s)

# Part 1

def compare(a, b):
    if idx == 1:
        print(a, b)
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif a == b:
            return None
        else:
            return False
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if i >= len(b):
                return False
            c = compare(a[i], b[i])
            if c in {False, True}:
                return c
        if len(b) > len(a):
            return True
        return None
    else: # different
        if isinstance(a, int):
            return compare([a], b)
        return compare(a, [b])
    return None


for idx, (a, b) in enumerate(lists):
    c = compare(a, b)
    if c is True:
        print('Yes')
        print(idx + 1)
        p1 += idx + 1
    elif c is False:
        print('No')
    elif c is None:
        assert False

print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
