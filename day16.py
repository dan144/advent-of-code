#!/usr/bin/python3.6

import re

sues = []
with open('input/16', 'r') as f:
    for line in f:
        groups = re.findall(r'(children: \d+|cats: \d+|samoyeds: \d+|pomeranians: \d+|akitas: \d+|vizslas: \d+|goldfish: \d+|trees: \d+|cars: \d+|perfumes: \d+)', line)
        d = {x.split(': ')[0]: int(x.split(': ')[1]) for x in groups}
        sues.append(d)

exp = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for sue in sues:
    for k, v in exp.items():
        if sue.get(k) is not None and sue.get(k) != v:
            break
    else:
        print(f'Part 1: {sues.index(sue) + 1}')
        break
