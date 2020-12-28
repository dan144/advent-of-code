#!/usr/bin/env python3

import hashlib
import re
import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 0

with open(input_file) as f:
    num = f.readline().rstrip()

def run(extra):
    keys = []
    maybe = []
    counter = 0
    while len(keys) < 64 or maybe:
        if counter % 1000 == 0:
            print(f'\rChecking {counter}', end='')
        digest = hashlib.md5(num.encode() + str(counter).encode()).hexdigest()
        if extra:
            for _ in range(2016):
                digest = hashlib.md5(digest.encode()).hexdigest()
    
        triple = False
        for i, c in enumerate(digest[:-2]):
            if c == digest[i + 1] == digest[i + 2]:
                triple = c
                break
    
        for key, c, idx in copy(maybe):
            if idx + 1000 < counter:
                maybe.remove((key, c, idx))
                continue
            if c * 5 in digest:
                keys.append((key, idx))
                maybe.remove((key, c, idx))
    
        if triple and len(keys) < 64:
            maybe.append((digest, triple, counter))
    
        counter += 1
    return sorted(keys, key=lambda x: x[1])

keys = run(False)
print()
p1 = keys[63][1]
print(f'Part 1: {p1}')

keys = run(True)
print()
p2 = keys[63][1]
print(f'Part 2: {p2}')
