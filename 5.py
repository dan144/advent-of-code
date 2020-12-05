#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file, 'r') as f:
    ids = {int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for line in f}

print(f'Part 1: {max(ids)}')
print(f'Part 2: {(set(range(min(ids), max(ids) + 1)) - ids).pop()}')
