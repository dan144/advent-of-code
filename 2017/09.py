#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 0

inp = []
with open(input_file) as f:
    inp = f.readline().rstrip()

# remove !.
while '!' in inp:
    l = inp.index('!')
    inp = inp[:l] + inp[l+2:]

# remove garbage, counting its len
match = True
while match:
    match = re.search(r'<[^>]*>', inp)
    if match:
        inp = inp[:match.start()] + inp[match.end():]
        p2 += match.end() - match.start() - 2

def dig(l, level):
    t = level
    for i in l:
        t += dig(i, level + 1)
    return t

# recursively measure by evaluating as nested lists
inp = inp.replace('{', '[').replace('}', ']')
inp = inp.replace(',]', ']').replace('[,', '[')
p1 = dig(eval(inp), 1)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
