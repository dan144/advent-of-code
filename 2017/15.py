#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

starts = []
with open(input_file) as f:
    for line in f:
        starts.append(int(line.rstrip().split()[-1]))

gen_a, gen_b = starts

a_factor = 16807
b_factor = 48271
div = 2147483647

for n in range(40000000):
    if n % 100000 == 0:
        print(f'\r{n}', end='')
    gen_a = (gen_a * a_factor) % div
    gen_b = (gen_b * b_factor) % div
    if gen_a % 2**16 == gen_b % 2**16:
        p1 += 1
print(f'\nPart 1: {p1}')

from_a = None
from_b = None
compute_a = True
compute_b = True
p = 0
n = 0
while p < 5000000:
    n += 1
    if p % 10000 == 0:
        print(f'\r{p}', end='')

    if from_a is None:
        gen_a = (gen_a * a_factor) % div
    if from_b is None:
        gen_b = (gen_b * b_factor) % div

    if gen_a % 4 == 0:
        from_a = gen_a
    if gen_b % 8 == 0:
        from_b = gen_b

    if from_a and from_b:
        p += 1
        if from_a % 2**16 == from_b % 2**16:
            p2 += 1
        from_a = None
        from_b = None

print(f'\nPart 2: {p2}')
