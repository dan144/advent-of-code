#!/usr/bin/env python3

import re
import sys

from computer import parse, run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

rules = {}
strs = []
to_strs = False
with open(input_file) as f:
    for line in f:
        if line == '\n':
            to_strs = True
            continue
        line = line[:-1]
        if to_strs:
            strs.append(line)
        else:
            n, r = line.split(' ', 1)
            rs = []
            for s in r.split('|'):
                rs.append(s.strip().split())
            rules[int(n.rstrip(':'))] = rs
                
def generate(rule_set, pre):
    subs = []
    for sub in rule_set:
        try:
            r = ''
            for rule in sub:
                try:
                    rule = int(rule)
                    x = generate(rules[rule], pre + [rule])
                    if isinstance(x, list):
                        x = f'({"|".join(x)})' if len(x) > 1 else x[0]
                    r += x
                except ValueError:
                    r = eval(rule)
            subs.append(r)
        except TypeError:
            subs.append(eval(sub[0]))
    return subs

rule = generate(rules[0], [])
print(rule[0])
for s in strs:
    p1 += bool(re.fullmatch(rule[0], s))

print(f'Part 1: {p1}')


print(f'Part 2: {p2}')
