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
    for line in f:
        inputs.append(data_type(line[:-1]))
if testing:
    print(inputs)

print()
print('PART ONE')
ans = None

#2,5,-4,-7
consts = []
for line in inputs:
    consts.append([tuple(map(int, line.split(',')))])

def man_dist(a, b):
    d = 0
    for i in range(4):
        d += abs(a[i]-b[i])
    return d

new = True
while new:
    new = False
    n = []
    removed = set()
    for i in range(len(consts) - 1):
        if i in removed:
            continue
        for j in range(i+1, len(consts)):
            if j in removed:
                continue
            for a in consts[i]:
                for b in consts[j]:
                    if man_dist(a, b) <= 3:
                        consts[i].extend(consts[j])
                        new = True
                        removed.add(j)
                        break
                else:
                    continue
                break
    for r in sorted(removed, reverse=True):
        consts.pop(r)

ans = len(consts)
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')
