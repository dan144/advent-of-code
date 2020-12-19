#!/usr/bin/env python3

import re
import sys

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
                
def generate(rule_set, n, pre, part2):
    subs = []
    for sub in rule_set[n]:
        r = []
        for rule in sub:
            try:
                rule = int(rule)
                if rule in pre:
                    continue # don't cycle
                x = generate(rules, rule, pre + [rule], part2)
                if isinstance(x, list):
                    x = f'({"|".join(x)})' if len(x) > 1 else x[0]
                if part2 and n == 8:
                    x += '+'
                r.append(x)
            except ValueError:
                r = [eval(rule)]
        subs.append(''.join(r))
    return subs

rule = generate(rules, 0, [], False)
for s in strs:
    p1 += bool(re.fullmatch(rule[0], s))

print(f'Part 1: {p1}')

# new 8: any # of rule 42
# new 11: any # of rule 42, then same # of 31
rules[8] = [['42', '8']]
rules[11] = [
    ['42', '31'],
    ['42', '42', '31', '31'],
    ['42', '42', '42', '31', '31', '31'],
    ['42', '42', '42', '42', '31', '31', '31', '31'],
    ['42', '42', '42', '42', '42', '31', '31', '31', '31', '31'],
    ['42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31'],
]
rule = generate(rules, 0, [], True)
for s in strs:
    p2 += bool(re.fullmatch(rule[0], s))
print(f'Part 2: {p2}')
