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

print()
print('PART ONE')
ans = None

ipr = int(inputs.pop(0).split()[1])
ins = []
for line in inputs:
    i = line.split(' ', 4)[:4]
    ins.append((i[0], int(i[1]), int(i[2]), int(i[3])))

r = [0] * 6

ip = 0
while ip in range(len(ins)):
    r[ipr] = ip
    i = ins[ip]
    #r[i[3]] = getattr('day19.py', i[0])(r, i)
    r[i[3]] = locals()[i[0]](r, i)
    ip = r[ipr] + 1
    print(ip, r)

ans = r[0]
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
