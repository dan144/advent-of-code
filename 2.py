#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file, 'r') as f:
    for line in f:
        rng, letter, password = line.split()
        letter = letter.rstrip(':')
        mn, mx = map(int, rng.split('-'))
        l_c = 0
        for c in password:
            if c == letter:
                l_c += 1
        if l_c >= mn and l_c <= mx:
            p1 += 1

        if (password[mn-1] == letter and password[mx-1] != letter) or (password[mn-1] != letter and password[mx-1] == letter):
            p2 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
