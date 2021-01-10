#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    tr, tc = map(int, re.findall(r'\d+', f.readline()))

mul = 252533
div = 33554393

def nx(n):
    return (n * mul) % div

r = 1
c = 1
layer = 1
p1 = 20151125
while True:
    if r == tr and c == tc:
        break
    p1 = nx(p1)
    if r == 1:
        layer += 1
        c = 1
        r = layer
    else:
        r -= 1
        c += 1

print(f'Part 1: {p1}')
