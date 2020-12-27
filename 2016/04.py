#!/usr/bin/env python3

import re
import string
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.rstrip())

def decrypt(room, ID):
    name = ''
    for c in room:
        if c == '-':
            name += ' '
        else:
            n = string.ascii_lowercase.index(c)
            n = (n + ID) % 26
            name += string.ascii_lowercase[n]
    if 'north' in name:
        print(f'{ID}: {name}')

for line in inp:
    m = re.match(r'([a-z-]+)-(\d+)\[([a-z]{5})\]', line)
    room, ID, check = m.groups()
    counts = {}
    for s in string.ascii_lowercase:
        counts[s] = room.count(s)
    s = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    most_str = []
    while True:
        most = []
        while s:
            most.append(s.pop(0))
            if not s:
                break
            if most[-1][1] > s[0][1]:
                break

        most_str.extend([x[0] for x in most])
        if len(most_str) > 5:
            most_str = most_str[:5]
        if len(most_str) == 5:
            break

    if sorted(most_str) == sorted(list(check)):
        p1 += int(ID)
        decrypt(room, int(ID))

print(f'Part 1: {p1}')
