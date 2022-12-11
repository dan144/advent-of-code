#!/usr/bin/env python3

import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

monkeys = {}
business = {}
with open(input_file) as f:
    for line in f:
        line = line.strip().split()
        if not line:
            continue
        if line[0] == 'Monkey':
            monkey = int(line[1].rstrip(':'))
            monkeys[monkey] = {}
            business[monkey] = 0
        elif line[0] == 'Starting':
            items = eval(' '.join(line[2:]))
            if isinstance(items, int):
                monkeys[monkey]['items'] = [items]
            else:
                monkeys[monkey]['items'] = []
                for item in items:
                    monkeys[monkey]['items'].append(int(item))
        elif line[0] == 'Operation:':
            monkeys[monkey]['op'] = ' '.join(line[3:])
        elif line[0] == 'Test:':
            monkeys[monkey]['test'] = int(line[-1])
        elif line[1] == 'true:':
            monkeys[monkey]['true'] = int(line[-1])
        elif line[1] == 'false:':
            monkeys[monkey]['false'] = int(line[-1])

# Part 1
for monkey in monkeys.keys():
    pass #print(monkey)

for r in range(20):
    print(r)
    new_monkeys = deepcopy(monkeys)
    for monkey in new_monkeys.keys():
        new_monkeys[monkey]['items'] = []

    monkey_list = monkeys.keys()
    for monkey in monkey_list:
        value = monkeys[monkey]
        for item in value['items']:
            business[monkey] += 1
            #print(item)
            worry = eval(value['op'].replace('old', str(item)))
            #print(worry)
            worry //= 3
            #print(worry)
            if worry % value['test'] == 0:
                give_to = value['true']
            else:
                give_to = value['false']
            #print(give_to)
            monkeys[give_to]['items'].append(worry)
        monkeys[monkey]['items'] = []
            #input()
    #monkeys = new_monkeys

print(business)
vals = sorted(business.values(), reverse=True)
p1 = vals[0] * vals[1]
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')