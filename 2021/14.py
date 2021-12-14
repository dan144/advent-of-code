#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

ins = {}
polymer = {}
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if not polymer:
            for i in range(len(line)-1):
                a, b = line[i:i+2]
                if a + b not in polymer:
                    polymer[a + b] = 0
                polymer[a + b] += 1

            # save for later
            first = line[0]
            last = line[-1]
        else:
            o, n = line.split(' -> ')
            ins[o] = n

def count():
    # compute occurrences of each letter
    occs = {}
    for x, n in polymer.items():
        for count in x:
            if count not in occs:
                occs[count] = 0
            occs[count] += n

    # adjust for first/last letter before halving all
    occs[first] += 1
    occs[last] += 1
    for k in occs.keys():
        occs[k] //= 2

    v = sorted(occs.values())
    return v[-1] - v[0]

for step in range(40):
    new = {}
    for x, count in polymer.items():
        a, b = x
        n = ins[x]
        for v in (a + n, n + b):
            if v not in new:
                new[v] = 0
            new[v] += count
    polymer = new

    if step == 9:
        p1 = count()
p2 = count()

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
