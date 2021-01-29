#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

transf = {}
with open(input_file) as f:
    for line in f:
        i, o = line.split(' => ')
        transf[i] = o

### reused from my 2020 day 20 solution
# taken from https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/
def do_rotate(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A
# end copy

def do_yflip(chunk):
    return chunk[::-1]

def do_xflip(chunk):
    for r in range(len(chunk)):
        chunk[r] = chunk[r][::-1]
    return chunk
### end reuse

def convert(chunk):
    c = []
    for row in chunk:
        c.append(''.join(row))
    return '/'.join(c)

def run(iterations):
    grid = utils.parse_grid(['.#.', '..#', '###'])
    for iteration in range(iterations):
        print(f'\r{iteration}', end='')
        dims = utils.get_grid_edges(grid)
        size = dims[2] - dims[0] + 1
        if size % 2 == 0:
            chunk_size = 2
        else:
            chunk_size = 3
        n_chunk_size = chunk_size + 1
    
        n_grid = {}
        for x in range(size // chunk_size):
            for y in range(size // chunk_size):
                chunk = []
                for dx in range(chunk_size):
                    row = []
                    for dy in range(chunk_size):
                        row += grid[x * chunk_size + dx, y * chunk_size + dy]
                    chunk.append(row)
    
                for i in range(16):
                    if i % 8 == 0:
                        chunk = do_xflip(chunk)
                    if i % 4 == 0 and i != 8:
                        chunk = do_yflip(chunk)
                    if i % 2 == 0:
                        chunk = do_rotate(chunk)
    
                    if convert(chunk) in transf:
                        break
                assert convert(chunk) in transf
    
                c = convert(chunk)
                for dx in range(n_chunk_size):
                    for dy in range(n_chunk_size):
                        n_grid[x * n_chunk_size + dx, y * n_chunk_size + dy] = transf[c].split('/')[dx][dy]
        grid = n_grid
    return grid

iterations = 2 if test else 5

grid = run(iterations)
p1 = sum([v == '#' for v in grid.values()])
print(f'\rPart 1: {p1}')

if not test:
    grid = run(18)
    p2 = sum([v == '#' for v in grid.values()])
    print(f'\rPart 2: {p2}')
