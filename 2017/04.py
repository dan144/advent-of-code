#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.rstrip().split())

for passphrase in inp:
    if len(passphrase) == len(set(passphrase)):
        p1 += 1
    else:
        continue
    valid = True
    for i, word1 in enumerate(passphrase):
        for j, word2 in enumerate(passphrase):
            if i == j:
                continue
            if sorted(word1) == sorted(word2):
                valid = False
    p2 += int(valid)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
