#!/usr/bin/python3

import json
import sys
import time

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
    return b[o[1]] + b[o[2]]

def addi(b, o):
    return b[o[1]] + o[2]
    
def mulr(b, o):
    return b[o[1]] * b[o[2]]
    
def muli(b, o):
    return b[o[1]] * o[2]

def banr(b, o):
    return b[o[1]] & b[o[2]]

def bani(b, o):
    return b[o[1]] & o[2]

def borr(b, o):
    return b[o[1]] | b[o[2]]

def bori(b, o):
    return b[o[1]] | o[2]

def setr(b, o):
    return b[o[1]]

def seti(b, o):
    return o[1]

def gtir(b, o):
    return int(o[1] > b[o[2]])

def gtri(b, o):
    return int(b[o[1]] > o[2])

def gtrr(b, o):
    return int(b[o[1]] > b[o[2]])

def eqir(b, o):
    return int(o[1] == b[o[2]])

def eqri(b, o):
    return int(b[o[1]] == o[2])

def eqrr(b, o):
    return (1 if (b[o[1]] == b[o[2]]) else 0)

ipr = int(inputs.pop(0).split()[1])
ins = []
for line in inputs:
    i = line.split(' ', 4)[:4]
    ins.append((i[0], int(i[1]), int(i[2]), int(i[3])))

#  run the elfcode for this problem
#  if partOne, return the first found value. if not, return the last
#  this is extremely slow because this simulator is incredibly inefficient
def run(partOne):
    catchemall = set()
    r = [0, 0, 0, 0, 0, 0]
    ins_c = len(ins)

    last_found = time.time()
    while r[ipr] < ins_c:
        r[ins[r[ipr]][3]] = globals()[ins[r[ipr]][0]](r, ins[r[ipr]])
        r[ipr] += 1
        if r[ipr] == 28:
            if r[3] not in catchemall:
                last_found = time.time()  # reset time last val was found
                if partOne:
                    return r[3]
                print(' {}    \r'.format(r[3]), end='')
                catchemall.add(r[3])
        # if it takes more than 5s to find the next acceptable value, assume you're done
        if time.time() - last_found > 5:
            return sorted(catchemall)[-1]

print()
print('PART ONE')

ans = run(True)

print('{}   '.format(ans))
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')

ans = run(False)

print('{}   '.format(ans))
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
