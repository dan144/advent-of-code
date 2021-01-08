#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

disks = []
with open(input_file) as f:
    for line in f:
        disks.append(list(map(int, re.findall(r'\d+', line))))

def run(disks):
    t = 0
    while True:
        for num, n_pos, _, pos in disks:
            pos_when_at = (pos + num + t) % n_pos
            if pos_when_at == 0:
                continue
            break
        else:
            break
        t += 1
    return t

p1 = run(disks)
print(f'Part 1: {p1}')

new_disk = [max(set(disk[0] for disk in disks)) + 1, 11, 0, 0]
disks.append(new_disk)
p2 = run(disks)
print(f'Part 2: {p2}')
