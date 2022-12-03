#!/usr/bin/env python3

import string
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

i = 0
sacks = []
with open(input_file) as f:
    for line in f:
        sack = line.strip()

        l = len(sack)
        same = (set(sack[:l//2]) & set(sack[l//2:])).pop()
        if same in string.ascii_lowercase:
            p1 += string.ascii_lowercase.index(same) + 1
        elif same in string.ascii_uppercase:
            p1 += string.ascii_uppercase.index(same) + 27

        i += 1
        sacks.append(set(sack))
        if i % 3 == 0:
            same = (sacks[-3] & sacks[-2] & sacks[-1]).pop()
            if same in string.ascii_lowercase:
                p2 += string.ascii_lowercase.index(same) + 1
            elif same in string.ascii_uppercase:
                p2 += string.ascii_uppercase.index(same) + 27

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
