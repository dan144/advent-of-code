#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

def fill(l_addr, val):
    if 'X' in l_addr:
        fill(l_addr.replace('X', '0', 1), val)
        fill(l_addr.replace('X', '1', 1), val)
    else:
        addr = int(l_addr, 2)
        if addr not in mem:
            mem[addr] = 0
        mem[addr] = (omask & val) | zmask

mem = {}
with open(input_file) as f:
    for line in f:
        if line.startswith('mask = '):
            mask = line.split(' = ')[1].rstrip('\n')
            zmask = int(mask.replace('X', '0'), 2)
            omask = int(mask.replace('X', '1'), 2)
        else:
            addr, val = map(int, re.findall(r'[0-9]+', line))
            l_addr = '{0:036b}'.format(addr)
            fill(l_addr, val)

p1 = sum(mem.values())
print(f'Part 1: {p1}')

omask = 2 ** 36 - 1
zmask = 0
mem = {}
with open(input_file) as f:
    for line in f:
        if line.startswith('mask = '):
            mask = list(line.split(' = ')[1].rstrip('\n'))
        else:
            addr, val = map(int, re.findall(r'[0-9]+', line))
            l_addr = list('{0:036b}'.format(addr))
            addr = ''.join((mask[b] if mask[b] in 'X1' else l_addr[b] for b in range(len(mask))))
            fill(addr, val)

p2 = sum(mem.values())
print(f'Part 2: {p2}')
