#!/usr/bin/env python3

import re
import sys

from computer import parse, run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    val = list(map(int, list(f.readline()[:-1])))
mx = max(val)
while len(val) < 1000000:
    val.append(mx + 1)
    mx = max(val)

next_cup = val[0]
for move in range(10000000): #10 if test else 100):
    look_at = val.index(next_cup)
    if move % 100 == 0:
        print('Move:', move)
    current = val[look_at]
    #print('cups:', val, f'({current})')
    n = 3
    new = []
    for i in range(n):
        idx = look_at + 1
        if idx >= len(val):
            idx = 0
        n = val.pop(idx)
        new.append(n)
    idx = look_at + 1
    if idx >= len(val):
        idx = 0
    next_cup = val[idx]
    #print('pick up:', new)
    while True:
        try:
            put_at = val.index(current - 1)
            break
        except ValueError:
            current -= 1
            if current < 0:
                current = mx + 1
    dest = val[put_at]
    #print('destination:', val[put_at])
    idx = val.index(dest)
    val = val[:idx+1] + new + val[idx+1:]

idx = val.index(1)
p2 = val[idx + 1] * val[idx + 2]
# p1 = ''.join(map(str, val[idx+1:] + val[:idx]))
print(f'Part 1: {p1}')


print(f'Part 2: {p2}')
