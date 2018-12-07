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

workers = 5
base_time = 60
t = 0
work = []
ans = ''
while remain or work:
    remain.sort()
    for w in range(len(work), workers):
        if remain:
            work.append([remain[0], 0, base_time + 1 + ord(remain[0]) - ord('A')])
            remain = remain[1:]
        else:
            break
    t += 1
    to_remove = []
    for i in range(len(work)):
        w = work[i]
        w[1] += 1
        if w[1] == w[2]:
            ans += w[0]
            to_remove.append(w)
    to_add = []
    for l, _, _ in to_remove:
        for letter, needs in data.items():
            if l in needs:
                data[letter].remove(l)
            if data[letter] == []:
                to_add.append(letter)
    for l in to_remove:
        work.remove(l)
    for letter in to_add:
        remain.append(letter)
        data.pop(letter)
    #print(ans, remain, work)
print(t)
