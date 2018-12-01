#!/usr/bin/python3

import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:',input_file)

total = 0
totals = []
ans = None
while not ans:
    if totals == []:
        totals = [0]
    with open(input_file, 'r') as f:
        for line in f:
            if line[0] == "+":
                total += int(line[1:])
            elif line[0] == '-':
                total -= int(line[1:])
            else:
                continue
            #print(line)
            if total in totals:
                ans = total
                break
            else:
                totals.append(total)
    #print(len(totals), totals[-1])
print(ans)
