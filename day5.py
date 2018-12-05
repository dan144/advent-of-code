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

val = list(inputs[0])
print('Original polymer length:', len(val))
removed = True
while removed:
    removed = False
    try:
        for i in range(len(val) - 1):
            if val[i].isupper() and val[i+1].islower():
                if val[i].lower() == val[i+1]:
                    val.pop(i)
                    val.pop(i)
                    i -= 1
                    removed = True
            if val[i].islower() and val[i+1].isupper():
                if val[i].upper() == val[i+1]:
                    val.pop(i)
                    val.pop(i)
                    i -= 1
                    removed = True
    except IndexError:
        continue
print('Reacted polymer length: ', len(val))

print()
print('PART TWO')

min_polymer_len = None
min_letter = None
for letter in string.ascii_lowercase:
    val = []
    for c in list(inputs[0]):
        if c.lower() != letter:
            val.append(c)
    removed = True
    while removed:
        removed = False
        try:
            for i in range(len(val) - 1):
                if val[i].isupper() and val[i+1].islower():
                    if val[i].lower() == val[i+1]:
                        val.pop(i)
                        val.pop(i)
                        i -= 1
                        removed = True
                if val[i].islower() and val[i+1].isupper():
                    if val[i].upper() == val[i+1]:
                        val.pop(i)
                        val.pop(i)
                        i -= 1
                        removed = True
        except IndexError:
            continue
    print('Removing', letter, 'gives', len(val))
    if min_polymer_len is None or len(val) < min_polymer_len:
        min_letter = letter
        min_polymer_len = len(val)
print('Removed', min_letter, 'to get minimum polymer length', min_polymer_len)
