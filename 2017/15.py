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

from_a = []
from_b = []
p = 5000001
n = 0
while n <= 40000000 or p <= 5000000:
    if n % 100000 == 0:
        print(f'\r{n} {p}', end='')
    gen_a = (gen_a * a_factor) % div
    gen_b = (gen_b * b_factor) % div
    if n <= 40000000:
        if gen_a % 2**16 == gen_b % 2**16:
            p1 += 1
        if n == 40000000:
            print(f'\nPart 1: {p1}')

    #if gen_a % 4 == 0:
    #    from_a.append(gen_a)
    #if gen_b % 8 == 0:
    #    from_b.append(gen_b)

    #if from_a and from_b:
    #    p += 1
    #    a = from_a.pop(0)
    #    b = from_b.pop(0)
    #    if a % 2**16 == b % 2**16:
    #        p2 += 1
    n += 1

print(f'\nPart 2: {p2}')
