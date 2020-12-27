#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    inp = f.readline().rstrip()

paren = re.compile('\(\d+x\d+\)')
r = re.compile('[A-Z]|\(\d+x\d+\)')
markers = r.findall(inp)
i = 0
while i < len(markers):
    j = i
    try:
        while '(' not in markers[j]:
            j += 1
    except IndexError:
        break

    marker = markers[j]
    c, n = map(int, re.findall(r'\d+', marker))
    new = []
    while len(''.join(new)) != c:
        new.append(markers.pop(j + 1))
    markers = markers[:j] + new * n + markers[j+1:]
    i = j + len(new) * n

p1 = len(''.join(markers))
print(f'Part 1: {p1}')

def dig(markers):
    total = 0
    i = 0
    while i < len(markers):
        if '(' in markers[i]:
            c, n = map(int, re.findall(r'\d+', marker))
            new = []
            j = i + 1
            while len(''.join(new)) != c:
                new.append(markers.pop(j + 1))
            total += n * dig(new * n + markers[j+1:])
        i += 1
    return total

markers = r.findall(inp)
p2 = dig(markers)
print(f'Part 2: {p2}')
