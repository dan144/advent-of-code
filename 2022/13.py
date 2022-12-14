#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 1

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

def compare(a, b):
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
        p1 += idx + 1
    elif c is None:
        assert False

# Part 1
print(f'Part 1: {p1}')

# Part 2

all_lists = [[[2]], [[6]]]
for a, b in lists:
    all_lists.extend([a, b])

sorted_lists = []
while all_lists:
    for a in all_lists:
        a_at_end = True
        for b in all_lists:
            if a == b:
                continue
            c = compare(a, b)
            if c is True: # is not at the end
                a_at_end = False
                break
        if a_at_end is True:
            break
    if a_at_end is True:
        sorted_lists = [a] + sorted_lists
        all_lists.remove(a)

for idx, a in enumerate(sorted_lists):
    if a == [[2]] or a == [[6]]:
        p2 *= idx + 1
print(f'Part 2: {p2}')
