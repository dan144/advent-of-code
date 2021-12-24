#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

ins = []
with open(input_file) as f:
    ins = utils.load_split_lines(f) # asdf asdf asdf ...

def get_inp():
    global r
    r += 1
    return str(input_val)[r]

# Part 1
input_val = 10**14
while True:
    if isinstance(input_val, list):
        input_val = int(''.join(input_val))
    input_val -= 1

    input_val = list(str(input_val))
    if '0' in input_val:
        continue
    if int(input_val[4]) - 1 != int(input_val[5]):
        if int(input_val[4]) > 1:
            input_val[5] = str(int(input_val[4]) - 1)
        else:
            input_val[5] = '0'
            continue
    if int(input_val[6]) - 3 != int(input_val[7]):
        if int(input_val[6]) > 3:
            input_val[7] = str(int(input_val[6]) - 3)
        else:
            input_val[6] = '0'
            continue
    if int(input_val[3]) - 5 != int(input_val[8]):
        if int(input_val[5]) > 5:
            input_val[8] = str(int(input_val[3]) - 5)
        else:
            input_val[3] = '0'
            continue
    if int(input_val[10]) - 5 != int(input_val[9]):
        if int(input_val[10]) > 5:
            input_val[9] = str(int(input_val[10]) - 5)
        else:
            input_val[10] = '0'
            continue
    if int(input_val[11]) - 7 != int(input_val[2]):
        if int(input_val[11]) > 7:
            input_val[2] = str(int(input_val[11]) - 7)
        else:
            input_val[2] = '0'
            continue
    if int(input_val[12]) - 3 != int(input_val[1]):
        if int(input_val[12]) > 3:
            input_val[1] = str(int(input_val[12]) - 3)
        else:
            input_val[1] = '0'
            continue
    input_val = int(''.join(input_val))
    r = -1
    reg = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for n, i in enumerate(ins):
        cmd = i[0]
        a = i[1]
        if len(i) == 3:
            b = i[2]
    
        if cmd == 'inp':
            reg[a] = int(get_inp())
        elif cmd == 'add':
            try:
                reg[a] = reg.get(a, 0) + int(b)
            except:
                reg[a] = reg.get(a, 0) + reg[b]
        elif cmd == 'mul':
            try:
                reg[a] = reg.get(a, 0) * int(b)
            except:
                reg[a] = reg.get(a, 0) * reg[b]
        elif cmd == 'div':
            try:
                reg[a] = reg.get(a, 0) // int(b)
            except:
                reg[a] = reg.get(a, 0) // reg[b]
        elif cmd == 'mod':
            try:
                reg[a] = reg.get(a, 0) % int(b)
            except:
                reg[a] = reg.get(a, 0) % reg[b]
        elif cmd == 'eql':
            try:
                reg[a] = int(reg.get(a, 0) == int(b))
            except:
                reg[a] = int(reg.get(a, 0) == reg[b])
        else:
            assert False
    if reg['z'] == 0:
        break
p1 = input_val
print(f'Part 1: {p1}')

# Part 2
input_val = 31162141116841

while True:
    if isinstance(input_val, list):
        input_val = int(''.join(input_val))

    input_val = list(str(input_val))
    if '0' in input_val:
        continue
    if int(input_val[5]) + 1 != int(input_val[4]):
        continue
        if int(input_val[4]) < 8:
            input_val[4] = str(int(input_val[5]) + 1)
        else:
            continue
    if int(input_val[7]) + 3 != int(input_val[6]):
        continue
        if int(input_val[7]) < 6:
            input_val[6] = str(int(input_val[7]) + 3)
        else:
            continue
    if int(input_val[8]) + 5 != int(input_val[3]):
        continue
        if int(input_val[8]) < 4:
            input_val[3] = str(int(input_val[8]) + 5)
        else:
            continue
    if int(input_val[9]) + 5 != int(input_val[10]):
        continue
        if int(input_val[9]) < 4:
            input_val[10] = str(int(input_val[9]) + 5)
        else:
            continue
    if int(input_val[2]) + 7 != int(input_val[11]):
        continue
        if int(input_val[2]) < 2:
            input_val[11] = str(int(input_val[2]) + 7)
        else:
            continue
    if int(input_val[1]) + 3 != int(input_val[12]):
        continue
        if int(input_val[1]) < 6:
            input_val[12] = str(int(input_val[1]) + 3)
        else:
            continue
    if int(input_val[13]) + 2 != int(input_val[0]):
        continue
        if int(input_val[13]) < 7:
            input_val[0] = str(int(input_val[13]) + 2)
        else:
            continue
    input_val = int(''.join(input_val))
    r = -1
    reg = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for n, i in enumerate(ins):
        cmd = i[0]
        a = i[1]
        if len(i) == 3:
            b = i[2]
    
        if cmd == 'inp':
            reg[a] = int(get_inp())
        elif cmd == 'add':
            try:
                reg[a] = reg.get(a, 0) + int(b)
            except:
                reg[a] = reg.get(a, 0) + reg[b]
        elif cmd == 'mul':
            try:
                reg[a] = reg.get(a, 0) * int(b)
            except:
                reg[a] = reg.get(a, 0) * reg[b]
        elif cmd == 'div':
            try:
                reg[a] = reg.get(a, 0) // int(b)
            except:
                reg[a] = reg.get(a, 0) // reg[b]
        elif cmd == 'mod':
            try:
                reg[a] = reg.get(a, 0) % int(b)
            except:
                reg[a] = reg.get(a, 0) % reg[b]
        elif cmd == 'eql':
            try:
                reg[a] = int(reg.get(a, 0) == int(b))
            except:
                reg[a] = int(reg.get(a, 0) == reg[b])
        else:
            assert False
    if reg['z'] == 0:
        break
    input_val += 1

p2 = input_val
print(f'Part 2: {p2}')
