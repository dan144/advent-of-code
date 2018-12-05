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

print()
print('PART ONE')

val = []
print('Original polymer length:', len(inputs[0]))
for c in inputs[0]:
    if len(val) > 0:
        if c.isupper() and val[-1].islower() and c.lower() == val[-1]:
            val.pop()
            continue
        if c.islower() and val[-1].isupper() and c.upper() == val[-1]:
            val.pop()
            continue
    val.append(c)
print('Reacted polymer length: ', len(val))

print()
print('PART TWO')

min_polymer_len = None
min_letter = None
for letter in string.ascii_lowercase:
    val = []
    for c in inputs[0]:
        if c.lower() == letter:
            continue
        if len(val) > 0:
            if c.isupper() and val[-1].islower() and c.lower() == val[-1]:
                val.pop()
                continue
            if c.islower() and val[-1].isupper() and c.upper() == val[-1]:
                val.pop()
                continue
        val.append(c)
    if min_polymer_len is None or len(val) < min_polymer_len:
        min_letter = letter
        min_polymer_len = len(val)
print('Removed', min_letter, 'to get minimum polymer length', min_polymer_len)
