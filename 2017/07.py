#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

programs = {}
with open(input_file) as f:
    for line in f:
        name, weight, above = re.match(r'([a-z]+) \((\d+)\)(?: -> )*((?:[a-z]+,? ?)+)?', line).groups()
        if above:
            above = above.split(', ')
        programs[name] = [int(weight), above or []]

supported = set()
for _, above in programs.values():
    supported.update(above)

p1 = set(programs.keys()) - supported
p1 = p1.pop()
print(f'Part 1: {p1}')

def check_balance(tower, levels, level):
    data = programs[tower]
    weight = data[0]
    for above in data[1]:
        weight += check_balance(above, levels, level + 1)

    if level in levels:
        levels[level][weight] = levels[level].get(weight, 0) + 1
    else:
        levels[level] = {weight: 1}
    return weight

def dig_into(tower):
    weights = {}
    for above in programs[tower][1]:
        weight = check_balance(above, {}, 0)
        if weight in weights:
            weights[weight].add(above)
        else:
            weights[weight] = {above}
    
    odd_one = None
    for weight, found_in in weights.items():
        if len(found_in) == 1:
            odd_one = weight
        else:
            correct = weight

    if odd_one:
        to_change = weights[odd_one].pop()
        sub_change, sub_diff = dig_into(to_change)
        if sub_change is None:
            # everything below me is balanced, so I am the problem
            return to_change, correct - odd_one
        return sub_change, sub_diff

    # I was balanced
    return None, 0

change, difference = dig_into(p1)
p2 = programs[change][0] + difference
print(f'Part 2: {p2}')
