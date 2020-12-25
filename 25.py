#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(int(line.rstrip()))

card_pk, door_pk = inp

div_by = 20201227
subject_num = 7

def transform(val):
    val *= subject_num
    val = val % div_by
    return val

def run(val, subject_num, loop_size):
    for i in range(loop_size):
        val *= subject_num
        val = val % div_by
    return val

loop_size = 0
c_val = 1
d_val = 1
while True:
    loop_size += 1
    c_val = transform(c_val)
    d_val = transform(d_val)
    if c_val == card_pk:
        print('card')
        p1 = run(1, door_pk, loop_size)
        break
    if d_val == door_pk:
        print('door')
        p1 = run(1, card_pk, loop_size)
        break
print(loop_size)

print(f'Part 1: {p1}')
