#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

passports = []
passport = {}
with open(input_file, 'r') as f:
    for line in f:
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
            fields = line.split()
            for data in fields:
                k, v = data.split(':')
                passport[k] = v
passports.append(passport)

req = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}

for passport in passports:
    if len(passport.keys()) == 8 or set(passport.keys()) == req:
        p1 += 1
        valid = True
        for k, v in passport.items():
            if k == 'byr' and int(v) not in range(1920, 2002+1):
                valid = False
            if k == 'iyr' and int(v) not in range(2010, 2020+1):
                valid = False
            if k == 'eyr' and int(v) not in range(2020, 2030+1):
                valid = False
            if k == 'hgt':
                val = int(re.findall(r'[0-9]+', v)[0])
                if v.endswith('cm'):
                    if int(val) not in range(150, 193+1):
                        valid = False
                elif v.endswith('in'):
                    if int(val) not in range(59, 76+1):
                        valid = False
                else:
                    valid = False
            if k == 'hcl':
                try:
                    if len(re.findall(r'\#[a-f0-9]+', v)[0]) != 7:
                        valid = False
                except:
                    valid = False
            if k == 'ecl' and v not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                valid = False
            if k == 'pid':
                try:
                    l = len(re.findall(r'[0-9]+', v)[0])
                    if l != 9:
                        valid = False
                except:
                    valid = False
        if valid:
            p2 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
