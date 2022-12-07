#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

files = {}
mydir = ['/']
alldirs = set()
with open(input_file) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd[0] == '$': # is a command
            if cmd[1] == 'cd':
                if cmd[2] == '/':
                    mydir = ['/']
                elif cmd[2] == '..':
                    mydir.pop()
                elif cmd[2] != '.':
                    mydir.append(cmd[2])
            elif cmd[1] == 'ls': # print a dir
                alldirs.add(tuple(mydir))
        else: # is an ls output
            f = files
            for d in mydir:
                if d not in f:
                    f[d] = {}
                f = f[d]
            if cmd[0] != 'dir':
                f[cmd[1]] = int(cmd[0])

def get_size(files, dirs):
    # return the size of a dir, including subdirs
    f = files
    for d in dirs:
        f = f[d]

    size = 0
    for k, v in f.items():
        if isinstance(v, dict):
            size += get_size(files, dirs + (k,))
        else:
            size += v
    return size

# Part 1
dir_sizes = {}
for d in alldirs:
    size = get_size(files, d)
    if size <= 100000:
        p1 += size
    dir_sizes[d] = size

print(f'Part 1: {p1}')

# Part 2
free_space = 70000000 - get_size(files, ('/',))
needed_space = 30000000 - free_space
# equivalent: needed_space = get_size(files, ('/',)) - 40000000

for k, v in sorted(dir_sizes.items(), key=lambda x: x[1]):
    if v >= needed_space:
        print(f'Part 2: {v}')
        break
