#!/usr/bin/python3.6

import re

with open('input/12', 'r') as f:
    inp = f.read()

nums = re.findall(r'-?\d+', inp)
ans = sum(map(int, nums))
print(f'Part 1: {ans}')
