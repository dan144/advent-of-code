#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 0

inp = []
with open(input_file) as f:
    inp = f.readline().rstrip()

inp = re.sub(r'!.', '', inp)

# remove garbage, counting its len
for match in re.findall(r'<[^>]*>', inp):
    p2 += len(match) - 2
inp = re.sub(r'<[^>]*>', '', inp)

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
