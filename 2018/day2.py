#!/usr/bin/python3

import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:',input_file)

ids = []
with open(input_file, 'r') as f:
    for line in f:
        ids.append(line[:-1])

print()
print('PART ONE')
twos = 0
threes = 0
for line in ids:
    letters = {}
    for c in line:
        letters[c] = letters.get(c,0) + 1
    if 2 in letters.values():
        twos += 1
    if 3 in letters.values():
        threes += 1
print('Twos:    ', twos)
print('Threes:  ', threes)
print('Checksum:', twos*threes)

print()
print('PART TWO')
d = False
for i in ids:
    for j in ids:
        if i == j:
            continue
        diff = 0
        for n in range(len(i)):
            if i[n] != j[n]:
                if diff != 0:
                    diff = 0
                    break
                diff = n
        if diff != 0:
            print('Differing index:', diff)
            print('First id:       ', i)
            print('Second id:      ', j)
            print('Common letters: ', i[:diff] + i[diff+1:])
            break
    else:
        continue
    break
