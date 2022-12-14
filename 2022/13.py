#!/usr/bin/env python3

import sys

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
    # returns True or False if a decision is made; None to continue
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if i >= len(b): # right side ran out
                return False
            c = compare(a[i], b[i])
            if c in {False, True}: # only return if conclusive
                return c
        if len(b) > len(a): # left side ran out
            return True
        return None
    else: # different
        if isinstance(a, int):
            return compare([a], b)
        return compare(a, [b])
    return None


# Part 1
for idx, (a, b) in enumerate(lists):
    c = compare(a, b)
    assert c is not None
    if c is True:
        p1 += idx + 1
    elif c is None:
        assert False

print(f'Part 1: {p1}')

# Part 2
all_lists = [[[2]], [[6]]]
for a, b in lists:
    all_lists.extend([a, b])

while all_lists:
    for a in all_lists:
        a_at_end = True
        for b in all_lists:
            if a == b:
                continue
            c = compare(a, b)
            assert c is not None
            if c: # a is not at the end
                a_at_end = False
                break
        if a_at_end: # found it
            break
    if a_at_end is True:
        if a == [[2]] or a == [[6]]:
            p2 *= len(all_lists)
        all_lists.remove(a)

print(f'Part 2: {p2}')
