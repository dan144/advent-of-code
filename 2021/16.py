#!/usr/bin/env python3

import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# find_cheapest(grid, (y,x) start, (y,x) end) - grid of ints, finds cheapest path from start to end, returns cost dist
# transpose_grid(grid) - swap key values from (x, y) to (y, x) and back
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime
# adjs - set of dx,dy values for LRUD adjacencies
# diags - set of dx,dy values for diagonals
# all_dirs set of dx,dy values for all 8 surrounding values

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp = line.strip()

# Part 1
bits = []
for c in inp:
    b = bin(int(c, 16))[2:]
    while len(b) < 4:
        b = '0' + b
    bits.extend(list(b))

def get_n(bits, n):
    return ''.join(bits[:n]), bits[n:]

def parse(bits):
    packets = []
    print(bits)

    ver = ''
    for _ in range(3):
        ver += bits.pop(0)
    ver = int(ver, 2)

    typ = ''
    for _ in range(3):
        typ += bits.pop(0)
    typ = int(typ, 2)

    print(ver, typ)
    if typ == 4:
        val = ''
        last = False
        while True:
            if bits.pop(0) == '0':
                last = True
            n_val, bits = get_n(bits, 4)
            val += n_val
            if last:
                break
        val = int(val, 2)
        print(val)
        packets.append((ver, typ, val))
        return packets, bits
    else: # not 4, so operator
        l_type, bits = get_n(bits, 1)
        if l_type == '0': # specified bit len
            t_len, bits = get_n(bits, 15)
            t_len = int(t_len, 2)
            print('len', t_len)
            sub_pkts = []
            sub_bits, bits = get_n(bits, t_len)
            sub_bits = list(sub_bits)
            #while any(x == '1' for x in sub_bits):
            while sub_bits:
                p, sub_bits = parse(sub_bits)
                sub_pkts.extend(p)
            packets.append((ver, typ, sub_pkts))
            print(f'len {t_len} done')
        else: # specified sub packets
            sub_pkt, bits = get_n(bits, 11)
            sub_pkt = int(sub_pkt, 2)
            print('sub', sub_pkt)
            pkts = []
            for _ in range(sub_pkt):
                pkt, bits = parse(bits)
                pkts.extend(pkt)
            packets.append((ver, typ, pkts))
            print(f'sub {sub_pkt} done')

    return packets, bits

print(bits)
packets, bits = parse(bits)
print(packets)
print('end', bits)

def sum_ver(packets, op):
    total = 0
    print(packets)
    print('op', op)
    value = {
        0: 0,
        1: 1,
        2: float('inf'),
        3: 0,
        4: None,
        5: None,
        6: None,
        7: None,
        None: 0,
    }[op]

    for packet in packets:
        ver, typ, val = packet
        print(packet)

        total += ver
        sub = 0

        sub_val = val

        if isinstance(val, list):
            sub, sub_val = sum_ver(val, typ)
        total += sub

        if op == 0:
            value += sub_val
            print('added', value)
        elif op == 1:
            value *= sub_val
        elif op == 2:
            value = min(value, sub_val)
        elif op == 3:
            value = max(value, sub_val)
        elif op == 5:
            if value is None:
                value = sub_val
            else:
                value = 1 if value > sub_val else 0
        elif op == 6:
            if value is None:
                value = sub_val
            else:
                value = 1 if value < sub_val else 0
        elif op == 7:
            if value is None:
                value = sub_val
            else:
                value = 1 if value == sub_val else 0
        elif op is None:
            value = sub_val
    return total, value

print()
p1, p2 = sum_ver(packets, None)
print(f'Part 1: {p1}')

print(f'Part 2: {p2}')
