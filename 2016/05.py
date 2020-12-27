#!/usr/bin/env python3

import hashlib
import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = ''
p2 = [''] * 8

with open(input_file) as f:
    door = f.readline().rstrip()

counter = 0
while len(p1) < 8 or not(all(p2)):
    digest = hashlib.md5(door.encode() + str(counter).encode()).hexdigest()
    if digest.startswith('00000'):
        print(counter, digest)
        if len(p1) < 8:
            p1 += digest[5]

        try:
            pos = int(digest[5])
            if pos <= 7:
                if p2[pos] == '':
                    p2[pos] = digest[6]
        except ValueError:
            pass
    counter += 1

print(f'Part 1: {p1}')
p2 = ''.join(p2)
print(f'Part 2: {p2}')
