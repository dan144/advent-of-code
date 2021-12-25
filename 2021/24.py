#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

ins = []
with open(input_file) as f:
    ins = utils.load_split_lines(f) # asdf asdf asdf ...

def validate(input_val):
    r = 0
    reg = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for i in ins:
        cmd = i[0]
        a = i[1]
        if len(i) == 3:
            b = i[2]
    
        if cmd == 'inp':
            reg[a] = int(input_val[r])
            r += 1
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
            assert False # illegal cmd, should never happen
    return reg['z'] == 0


# Part 1
input_val = list(str(10**14))
while not validate(input_val):
    input_val = int(''.join(input_val)) - 1
    input_val = list(str(input_val))

    # this is a very ugly/inefficient way to enforce the rules for my input
    # requires specific differences between pairs of digits
    # to find the highest accepted value, enforce these rules in a downward fashion
    # the rule for the first digit and its partner is not here
    # but since this is the final digit, it has to resolve in maximum 8 tries
    if int(input_val[4]) - 1 != int(input_val[5]):
        if int(input_val[4]) > 1:
            input_val[5] = str(int(input_val[4]) - 1)
        else:
            input_val[4] = '0'
    if int(input_val[6]) - 3 != int(input_val[7]):
        if int(input_val[6]) > 3:
            input_val[7] = str(int(input_val[6]) - 3)
        else:
            input_val[6] = '0'
    if int(input_val[3]) - 5 != int(input_val[8]):
        if int(input_val[5]) > 5:
            input_val[8] = str(int(input_val[3]) - 5)
        else:
            input_val[3] = '0'
    if int(input_val[10]) - 5 != int(input_val[9]):
        if int(input_val[10]) > 5:
            input_val[9] = str(int(input_val[10]) - 5)
        else:
            input_val[10] = '0'
    if int(input_val[11]) - 7 != int(input_val[2]):
        if int(input_val[11]) > 7:
            input_val[2] = str(int(input_val[11]) - 7)
        else:
            input_val[2] = '0'
    if int(input_val[12]) - 3 != int(input_val[1]):
        if int(input_val[12]) > 3:
            input_val[1] = str(int(input_val[12]) - 3)
        else:
            input_val[1] = '0'

    if '0' in input_val: # no 0s allowed
        continue

p1 = ''.join(input_val)
print(f'Part 1: {p1}')

# Part 2
# we know the rules now, so let's just implement them and validate the result
input_val = [1] * 14
input_val[0] = input_val[13] + 2
input_val[3] = input_val[8] + 5
input_val[4] = input_val[5] + 1
input_val[6] = input_val[7] + 3
input_val[10] = input_val[9] + 5
input_val[11] = input_val[2] + 7
input_val[12] = input_val[1] + 3

p2 = ''.join((map(str, input_val)))
assert validate(p2)
print(f'Part 2: {p2}')
