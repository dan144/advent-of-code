#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    card_pk = int(f.readline().rstrip())
    door_pk = int(f.readline().rstrip())

def transform(val, subject_num):
    return (val * subject_num) % 20201227

def calculate(subject_num, loop_size):
    val = 1
    for i in range(loop_size):
        val = transform(val, subject_num)
    return val

loop_size = 1
c_val = 1
d_val = 1
while True:
    c_val = transform(c_val, 7)
    if c_val == card_pk:
        subject_num = door_pk
        break

    d_val = transform(d_val, 7)
    if d_val == door_pk:
        subject_num = card_pk
        break
    loop_size += 1

p1 = calculate(subject_num, loop_size)
print(f'Part 1: {p1}')
