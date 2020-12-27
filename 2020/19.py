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
            rule_num, rule_str = line.split(' ', 1)
            rule_set = []
            for s in rule_str.split('|'):
                rule_set.append(s.strip().split())
            rules[int(rule_num.rstrip(':'))] = rule_set
                
def generate(rule_num=0, pre=None, part2=False):
    # returns a list of expanded regexes
    pre = pre or []
    new_rules = []
    for rule_list in rules[rule_num]:
        sub_rules = []
        for rule in rule_list:
            try:
                rule = int(rule)
                gen = generate(rule, pre + [rule], part2)
                if isinstance(gen, list):
                    # a list means any is valid; combine with or
                    gen = f'({"|".join(gen)})' if len(gen) > 1 else gen[0]
                if part2 and rule_num == 8:
                    # new 8: any number of rule 42
                    gen = f'({gen})+'
                sub_rules.append(gen)
            except ValueError:
                # this is a letter, e.g. "x"
                sub_rules.append(eval(rule)) # eval clears the quotes
        new_rules.append(''.join(sub_rules))
    return new_rules if rule_num else new_rules[0]

rule = generate()
p1 = sum(bool(re.fullmatch(rule, s)) for s in strs)
print(f'Part 1: {p1}')

# new 11: any # of rule 42, then same # of 31
rules[11] = [
    ['42', '31'],
    ['42', '42', '31', '31'],
    ['42', '42', '42', '31', '31', '31'],
    ['42', '42', '42', '42', '31', '31', '31', '31'],
    ['42', '42', '42', '42', '42', '31', '31', '31', '31', '31'],
    ['42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31'],
]

rule = generate(part2=True)
p2 = sum(bool(re.fullmatch(rule, s)) for s in strs)
print(f'Part 2: {p2}')
