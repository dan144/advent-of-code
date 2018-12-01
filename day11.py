#!/usr/bin/python3

import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:',input_file)


with open(input_file, 'r') as f:
    for line in f:
        print(line)
