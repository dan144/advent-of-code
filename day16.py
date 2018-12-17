#!/usr/bin/python3

import json
import sys

print('Running:',sys.argv[0])

testing = len(sys.argv) == 2

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)

if testing:
    print('TESTING')
    input_file = 'test' + input_file

print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    if testing:
        test_vals = json.loads(f.readline())
        part_one = test_vals['part_one']
        part_two = test_vals['part_two']
    for line in f:
        inputs.append(data_type(line[:-1]))
if testing:
    print(inputs)

print()
print('PART ONE')
ans = None

#Before: [2, 3, 2, 2]
#0 3 3 0
#After:  [0, 3, 2, 2]

opsets = []
parsing = True
skipped = False
while parsing and inputs:
    line = inputs.pop(0)
    if line == '':
        if skipped:
            parsing = False
        skipped = True
    elif line.startswith('Before:'):
        op = []
        op.append(list(map(int, line.split('[', 1)[1][:-1].split(', '))))
        line = inputs.pop(0)
        op.append(list(map(int, line.split(' '))))
        line = inputs.pop(0)
        op.append(list(map(int, line.split('[', 1)[1][:-1].split(', '))))
        skipped = False
        opsets.append(op)

def addr(b, o, a):
    return a[o[3]] == (b[o[1]] + b[o[2]])

def addi(b, o, a):
    return a[o[3]] == (b[o[1]] + o[2])
    
def mulr(b, o, a):
    return a[o[3]] == (b[o[1]] * b[o[2]])
    
def muli(b, o, a):
    return a[o[3]] == (b[o[1]] * o[2])

def banr(b, o, a):
    return a[o[3]] == (b[o[1]] & b[o[2]])

def bani(b, o, a):
    return a[o[3]] == (b[o[1]] & o[2])

def borr(b, o, a):
    return a[o[3]] == (b[o[1]] | b[o[2]])

def bori(b, o, a):
    return a[o[3]] == (b[o[1]] | o[2])

def setr(b, o, a):
    return a[o[3]] == b[o[1]]

def seti(b, o, a):
    return a[o[3]] == o[1]

def gtir(b, o, a):
    return a[o[3]] == (1 if (o[1] > b[o[2]]) else 0)

def gtri(b, o, a):
    return a[o[3]] == (1 if (b[o[1]] > o[2]) else 0)

def gtrr(b, o, a):
    return a[o[3]] == (1 if (b[o[1]] > b[o[2]]) else 0)

def eqir(b, o, a):
    return a[o[3]] == (1 if (o[1] == b[o[2]]) else 0)

def eqri(b, o, a):
    return a[o[3]] == (1 if (b[o[1]] == o[2]) else 0)

def eqrr(b, o, a):
    return a[o[3]] == (1 if (b[o[1]] == b[o[2]]) else 0)

op_fs = (addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr)
op_is = [op_fs] * 16
def test_ops(opset):
    before, op, after = opset
    if testing:
        print(before, op, after)

    ops = 0
    for op_f in op_fs:
        if op_f(before, op, after):
            if testing:
                print(str(op_f))
            ops += 1

    return ops

print(len(opsets))
opcount = 0
for op in opsets:
    nops = test_ops(op)
    if nops >= 3:
        opcount += 1

ans = opcount
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')


print()
print('PART TWO')
ans = None



print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
