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

minn = None
catchemall = set()
def run_with_init(r0):
    global minn
    global catchemall
    r = [r0, 0, 0, 0, 0, 0]
    ip = 0
    ic = 0
    while ip in range(len(ins)):
        ic += 1
        r[ipr] = ip
        i = ins[ip]
        r[i[3]] = globals()[i[0]](r, i)
        ip = r[ipr] + 1
        #print(r)
        if ip == 28:
            print(r[3])
            sys.exit(1)
            catchemall.add(r[3])
            if minn is None or sorted(catchemall)[0] < minn:
                minn = sorted(catchemall)[0]
                print(ic, r, minn)
        print(ip, r)
        if ip in {13}: #{8,13,28}:
            input()
    print(ic)
    return True
    print('Done: r[0]={}, ic={}'.format(r0, ic))
    if minr[1] is None or ic < minr[1]:
        minr = [r0, ic]
    elif ic == minr[1] and r0 < minr[0]:
        minr = [r0, ic]

# FAIL: 8563139
# FAIL: 105934
# FAIL: 1634
r0 = 1634
while not run_with_init(r0):
    r0 += 1
    print(r0)
sys.exit(0)
import threading
threads = []
for r0 in range(1):
    t = threading.Thread(target=run_with_init, args=(r0,))
    print('Starting thread with r0={}'.format(r0))
    t.start()
    threads.append(t)
for t in threads:
    t.join()


ans = minr[0]
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
