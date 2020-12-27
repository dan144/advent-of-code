#!/usr/bin/python3

import json
import sys

from copy import copy

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

def addr(b, o):
    return (b[o[1]] + b[o[2]])

def addi(b, o):
    return (b[o[1]] + o[2])
    
def mulr(b, o):
    return (b[o[1]] * b[o[2]])
    
def muli(b, o):
    return (b[o[1]] * o[2])

def banr(b, o):
    return (b[o[1]] & b[o[2]])

def bani(b, o):
    return (b[o[1]] & o[2])

def borr(b, o):
    return (b[o[1]] | b[o[2]])

def bori(b, o):
    return (b[o[1]] | o[2])

def setr(b, o):
    return b[o[1]]

def seti(b, o):
    return o[1]

def gtir(b, o):
    return (1 if (o[1] > b[o[2]]) else 0)

def gtri(b, o):
    return (1 if (b[o[1]] > o[2]) else 0)

def gtrr(b, o):
    return (1 if (b[o[1]] > b[o[2]]) else 0)

def eqir(b, o):
    return (1 if (o[1] == b[o[2]]) else 0)

def eqri(b, o):
    return (1 if (b[o[1]] == o[2]) else 0)

def eqrr(b, o):
    return (1 if (b[o[1]] == b[o[2]]) else 0)

op_fs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
op_is = []
for i in range(16):
    op_is.append(copy(op_fs))
def test_ops(opset):
    before, op, after = opset
    if testing:
        print(before, op, after)

    ops = 0
    for op_f in op_fs:
        if op_f(before, op) == after[op[3]]:
            if testing:
                print(str(op_f))
            ops += 1
        elif op_f in op_is[op[0]]:  # this opcode could be this fuction
            op_is[op[0]].remove(op_f)

    return ops

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


def claim_op(i):
    for j in range(len(op_is)):
        if i != j and op_is[i][0] in op_is[j]:
            op_is[j].remove(op_is[i][0])
            if len(op_is[j]) == 1:
                claim_op(j)


for i in range(len(op_is)):
    if len(op_is[i]) == 1:
        claim_op(i)

for i in range(len(op_is)):
    if len(op_is[i]) == 1:
        op_is[i] = op_is[i][0]
        if testing:
            print(op_is[i])
    else:
        print('More than one possible opcode for opcode', i, '-', op_is[i])
        sys.exit(1)

cmds = []
for line in inputs:
    if line != '':
        cmds.append(list(map(int, line.split())))

r = [0, 0, 0, 0]
for cmd in cmds:
    r[cmd[3]] = op_is[cmd[0]](r, cmd)

ans = r[0]
print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
