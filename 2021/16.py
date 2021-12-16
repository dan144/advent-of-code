#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

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

    ver, bits = get_n(bits, 3)
    ver = int(ver, 2)

    typ, bits = get_n(bits, 3)
    typ = int(typ, 2)

    #print(ver, typ)
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
        #print(val)
        packets.append((ver, typ, val))
        return packets, bits
    else: # not 4, so operator
        l_type = bits.pop(0)
        if l_type == '0': # specified bit len
            t_len, bits = get_n(bits, 15)
            t_len = int(t_len, 2)
            #print('len', t_len)
            sub_pkts = []
            sub_bits, bits = get_n(bits, t_len)
            sub_bits = list(sub_bits)
            #while any(x == '1' for x in sub_bits):
            while sub_bits:
                p, sub_bits = parse(sub_bits)
                sub_pkts.extend(p)
            packets.append((ver, typ, sub_pkts))
            #print(f'len {t_len} done')
        else: # specified sub packets
            sub_pkt, bits = get_n(bits, 11)
            sub_pkt = int(sub_pkt, 2)
            #print('sub', sub_pkt)
            pkts = []
            for _ in range(sub_pkt):
                pkt, bits = parse(bits)
                pkts.extend(pkt)
            packets.append((ver, typ, pkts))
            #print(f'sub {sub_pkt} done')

    return packets, bits

#print(bits)
packets, bits = parse(bits)
#print(packets)
assert '1' not in bits # should end with only zeros

def sum_ver(packets, op):
    total = 0
    value = None
    #print('op', op)

    for packet in packets:
        ver, typ, val = packet
        #print(packet)

        total += ver
        sub = 0

        sub_val = val

        if isinstance(val, list):
            sub, sub_val = sum_ver(val, typ)
        total += sub

        value = {
            0: (value or 0) + sub_val,
            1: (0 if value == 0 else (value or 1)) * sub_val,
            2: min(value or float('inf'), sub_val),
            3: max(value or 0, sub_val),
            4: sub_val,
            5: sub_val if value is None else int(value > sub_val),
            6: sub_val if value is None else int(value < sub_val),
            7: sub_val if value is None else int(value == sub_val),
        }[op]

    return total, value

p1, p2 = sum_ver(packets, packets[0][1])
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
