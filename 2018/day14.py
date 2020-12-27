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

def parse():
    global last, ndig
    global r1, r2, e1, e2, recipes
    s = r1 + r2
    n1 = int(s / 10) if s >= 10 else None
    n2 = s % 10
    if n1:
        recipes += [n1, n2]
        last += [n1, n2]
    else:
        recipes += [n2]
        last += [n2]
    while len(last) >= ndig + 2:
        last = last[1:]
    e1 = (e1 + 1 + r1) % len(recipes)
    e2 = (e2 + 1 + r2) % len(recipes)
    r1 = recipes[e1]
    r2 = recipes[e2]
    return r1, r2, e1, e2

nrecipes = int(inputs[0])
r1 = 3
r2 = 7
recipes = [r1, r2]
e1 = 0
e2 = 1
last = [3, 7]
digs = list(map(int, str(nrecipes)))
ndig = len(str(nrecipes))

while len(recipes) < nrecipes + 11:
    r1, r2, e1, e2 = parse()

ans = ''.join(map(str, recipes[nrecipes:nrecipes + 10]))

print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')
ans = None

r1 = 3
r2 = 7
recipes = [r1, r2]
e1 = 0
e2 = 1
last = [3, 7]
while len(recipes) < ndig:
    r1, r2, e1, e2 = parse()
while True:
    r1, r2, e1, e2 = parse()
    if last[-1] == digs[-1] and last[1:] == digs:
        break
    elif last[-2] == digs[-1] and last[:-1] == digs:
        break

ans = len(recipes) - ndig - (1 if last[:-1] == digs else 0)

print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
