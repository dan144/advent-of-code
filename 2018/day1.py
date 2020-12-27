#!/usr/bin/python3

import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:',input_file)

diffs = []
with open(input_file, 'r') as f:
    for line in f:
        diffs.append(int(line[:-1]))

print()
print('PART ONE')
print('Sum:', sum(diffs))

print()
print('PART TWO')

total = 0
totals = None
ans = None
while not ans:
    if totals == None:
        totals = {0}
    for line in diffs:
        total += line
        #print(line)
        if total in totals:
            ans = total
            break
        else:
            totals.add(total)
    #print(len(totals), totals[-1])
print('First repeated:', ans)
