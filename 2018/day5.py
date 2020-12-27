#!/usr/bin/python3

import string
import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    for line in f:
        inputs.append(data_type(line[:-1]))

def reduce_polymer(inp, letter):
    val = []
    for c in inp:
        if letter and c.lower() == letter:
            continue
        if len(val) > 0:
            if c.isupper() and val[-1].islower() and c.lower() == val[-1]:
                val.pop()
                continue
            if c.islower() and val[-1].isupper() and c.upper() == val[-1]:
                val.pop()
                continue
        val.append(c)
    return val

print()
print('PART ONE')

print('Original polymer length:', len(inputs[0]))
val = reduce_polymer(inputs[0], None)
print('Reacted polymer length: ', len(val))

print()
print('PART TWO')

results = {}
for letter in string.ascii_lowercase:
    results[letter] = len(reduce_polymer(inputs[0], letter))
print('Minimum polymer length:', min(results.values()))
