#!/usr/bin/env python3

import re
import sys

from itertools import permutations

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.rstrip())

def run(use_s):
    s = list(use_s)
    for line in inp:
        tokens = line.split()
        if line.startswith('swap position'):
            x, y = int(tokens[2]), int(tokens[5])
            s[x], s[y] = s[y], s[x]
        elif line.startswith('swap letter'):
            a = tokens[2]
            b = tokens[5]
            x, y = s.index(a), s.index(b)
            s[x], s[y] = s[y], s[x]
        elif tokens[0] == 'rotate':
            if tokens[1] == 'based':
                based = True
                i = tokens[6]
                x = s.index(i) + 1
                if x > 4:
                    x += 1
            else:
                based = False
                x = int(tokens[2])

            if based or tokens[1] == 'right':
                for _ in range(x):
                    s = [s.pop(-1)] + s
            else:
                for _ in range(x):
                    s.append(s.pop(0))
        elif tokens[0] == 'reverse':
            vals = int(tokens[2]), int(tokens[4])
            x = min(vals)
            y = max(vals)
            n = []
            if x > 0:
                n = s[:x]
            v = s[x:y+1]
            n.extend(v[::-1])
            if y + 1 < len(s):
                n.extend(s[y+1:])
            s = n
        elif tokens[0] == 'move':
            x = int(tokens[2])
            y = int(tokens[5])
            v = s.pop(x)
            s.insert(y, v)
    return s

s = list('abcde' if test else 'abcdefgh')
p1 = ''.join(run(s))
print(f'Part 1: {p1}')

for use_s in permutations(s):
    if run(use_s) == list('fbgdceah'):
        break
else:
    raise
p2 = ''.join(use_s)
print(f'Part 2: {p2}')
