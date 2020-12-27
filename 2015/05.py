#!/usr/bin/env python3

import re
import string
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.rstrip())

for s in inp:
    if 'ab' not in s and 'cd' not in s and 'pq' not in s and 'xy' not in s:
        double = False
        for i, c in enumerate(s[:-1]):
            if s[i + 1] == c:
                double = True
                break
        if double:
            vowels = 0
            for c in s:
                vowels += c in 'aeiou'
            if vowels >= 3:
                p1 += 1

    surrounded = False
    for i, c in enumerate(s[:-3]):
        if s.count(c + s[i + 1]) >= 2:
            for letter1 in string.ascii_lowercase:
                if re.search(f'{letter1}[a-z]{letter1}', s):
                    surrounded = True
    p2 += surrounded

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
