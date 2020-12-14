#!/usr/bin/env python3

import re
import sys

from computer import parse, run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

mem = {}
with open(input_file) as f:
    mask = None
    for line in f:
        if line.startswith('mask = '):
            mask = line.split(' = ')[1].rstrip('\n')
            zmask = int(mask.replace('X', '0'), 2)
            mask = int(mask.replace('X', '1'), 2)
        else:
            addr, val = map(int, re.findall(r'[0-9]+', line))
            if addr in mem:
                mem[addr] = 0
            mem[addr] = (mask & val) | zmask

p1 = sum(mem.values())
print(f'Part 1: {p1}')

def fill(l_addr, val):
    if 'X' in l_addr:
        fill(l_addr.replace('X', '0', 1), val)
        fill(l_addr.replace('X', '1', 1), val)
    else:
        addr = int(l_addr, 2)
        if addr not in mem:
            mem[addr] = 0
        mem[addr] = val

mem = {}
with open(input_file) as f:
    mask = None
    for line in f:
        if line.startswith('mask = '):
            mask = list(line.split(' = ')[1].rstrip('\n'))
        else:
            addr, val = map(int, re.findall(r'[0-9]+', line))
            l_addr = list('{0:036b}'.format(addr))
            n_addr = []
            for b in range(len(mask)):
                bit = mask[b]
                if bit == 'X':
                    n_addr.append('X')
                elif bit == '1':
                    n_addr.append('1')
                else:
                    n_addr.append(l_addr[b])
            n_addr = ''.join(n_addr)
            mask = ''.join(mask)
            fill(n_addr, val)

p2 = sum(mem.values())
print(f'Part 2: {p2}')
