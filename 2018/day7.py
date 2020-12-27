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

orders = []
workers = 5
base_time = 60
with open(input_file, 'r') as f:
    if testing:
        test_vals = json.loads(f.readline())
        workers = test_vals['max_workers']
        base_time = test_vals['base_time']
        part_one = test_vals['part_one']
        part_two = test_vals['part_two']
    for line in f:
        orders.append([line.split()[1], line.split()[7]])
if testing:
    print(orders)

print()
print('PART ONE')

ans = ''
data = {}
for a, b in orders:
    if a not in data:
        data[a] = []
    if b not in data:
        data[b] = []
    data[b].append(a)
remain = []
for l, n in data.items():
    if n == []:
        remain.append(l)
for letter in remain:
    data.pop(letter)

while remain:
    remain.sort()
    l = remain[0]
    ans += l

    to_add = []
    for letter, needs in data.items():
        if l in needs:
            data[letter].remove(l)
        if data[letter] == []:
            to_add.append(letter)
    for letter in to_add:
        remain.append(letter)
        data.pop(letter)
    remain = remain[1:]

print(ans)
if testing:
    if ans == part_one:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')

data = {} # key/value will be letter/dependencies
for a, b in orders:
    if a not in data:
        data[a] = []
    if b not in data:
        data[b] = []
    data[b].append(a)

remain = []
for l, n in data.items():
    if n == []: # tasks with no initial dependencies
        remain.append(l)
for letter in remain:
    data.pop(letter)

t = 0
work = []
while remain or work:
    remain.sort()
    for w in range(len(work), workers): # add up to one job per worker
        if remain: # if there's remaining work
            # task, elapsed time, time to take
            work.append([remain[0], 0, base_time + 1 + ord(remain[0]) - ord('A')])
            remain = remain[1:]
        else:
            break

    t += 1
    to_remove = []
    for i in range(len(work)): # check for completed work
        w = work[i]
        w[1] += 1
        if w[1] == w[2]:
            to_remove.append(w)

    to_add = []
    for l, _, _ in to_remove: # check for tasks that can now be queued
        for letter, needs in data.items():
            if l in needs:
                data[letter].remove(l)
            if data[letter] == []:
                to_add.append(letter)

    for l in to_remove: # remove completed work
        work.remove(l)
    for letter in to_add: # add new work to start
        remain.append(letter)
        data.pop(letter)
print(t)
if testing:
    if t == part_two:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
