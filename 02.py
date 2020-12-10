#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file, 'r') as f:
    for line in f:
        rng, letter, password = line.split()
        letter = letter.rstrip(':')
        mn, mx = map(int, rng.split('-'))

        l_c = len(re.findall(letter, password))
        p1 += int(l_c in range(mn, mx+1))

        first = password[mn-1] == letter
        last = password[mx-1] == letter
        p2 += first ^ last

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
