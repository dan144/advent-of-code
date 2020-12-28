#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    num = f.readline().rstrip()

def extend(a):
    return a + '0' + a[::-1].replace('0', 'x').replace('1', '0').replace('x', '1')

a = num
mx = 12 if test else 272
while len(a) < mx:
    a = extend(a)
a = a[:mx]

def make_checksum(a):
    checksum = ''
    for i in range(0, len(a), 2):
        checksum += '1' if a[i] == a[i + 1] else '0'
    return checksum

while len(a) % 2 == 0:
    a = make_checksum(a)

p1 = a
print(f'Part 1: {p1}')

a = num
mx = 12 if test else 35651584
while len(a) < mx:
    a = extend(a)
a = a[:mx]

while len(a) % 2 == 0:
    a = make_checksum(a)

p2 = a
print(f'Part 2: {p2}')
