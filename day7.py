#!/usr/bin/python3

import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:', input_file)

orders = []
with open(input_file, 'r') as f:
    for line in f:
        orders.append([line.split()[1], line.split()[7]])
# Step T must be finished before step W can begin.

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

workers = 5
base_time = 60
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
