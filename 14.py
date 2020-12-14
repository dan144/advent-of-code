#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

def fill(addr, val):
    # takes address as a binary string and recurses for every X to reach all addrs
    if 'X' in addr:
        fill(addr.replace('X', '0', 1), val)
        fill(addr.replace('X', '1', 1), val)
    else:
        addr = int(addr, 2)
        if addr not in mem:
            mem[addr] = 0
        mem[addr] = (omask & val) | zmask

mem = {}
with open(input_file) as f:
    for line in f:
        if line.startswith('mask = '):
            mask = line.split(' = ')[1].rstrip('\n')
            zmask = int(mask.replace('X', '0'), 2) # do not replace on bitwise or
            omask = int(mask.replace('X', '1'), 2) # force replacement on bitwise and
        else:
            addr, val = map(int, re.findall(r'[0-9]+', line))
            fill(f'{addr:036b}', val)

p1 = sum(mem.values())
print(f'Part 1: {p1}')

# all ones and zeros to make it a pass through in fill()
omask = 2 ** 36 - 1
zmask = 0
mem = {}
with open(input_file) as f:
    for line in f:
        if line.startswith('mask = '):
            mask = list(line.split(' = ')[1].rstrip('\n'))
        else:
            i_addr, val = map(int, re.findall(r'[0-9]+', line))
            l_addr = list(f'{i_addr:036b}')
            # overwrite X and 1 from mask, pass through from address on 0
            addr = ''.join((mask[b] if mask[b] in 'X1' else l_addr[b] for b in range(len(mask))))
            fill(addr, val)

p2 = sum(mem.values())
print(f'Part 2: {p2}')
