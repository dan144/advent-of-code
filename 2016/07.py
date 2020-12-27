#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.rstrip())

def find_abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False

def find_aba(outside, hypernet):
    for s in outside:
        for i in range(len(s) - 2):
            if s[i] == s[i + 2] and s[i] != s[i + 1]:
                for h in hypernet:
                    if s[i + 1] + s[i] + s[i + 1] in h:
                        return True
    return False

re_inner = re.compile(r'\[([a-z]+)\]')
re_outside = re.compile(r'([a-z]+)')
for ip in inp:
    hypernet = re_inner.findall(ip)
    outside = re_outside.findall(ip)
    for h in hypernet:
        if h in outside:
            outside.remove(h)

    hyper, outer = False, False
    for h in hypernet:
        if find_abba(h):
            hyper = True
            break
    for o in outside:
        if find_abba(o):
            outer = True
            break
    if outer and not hyper:
        p1 += 1

    if find_aba(outside, hypernet):
        p2 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
