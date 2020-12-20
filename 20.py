#!/usr/bin/env python3

import re
import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 1
p2 = 0

tiles = {}
in_tile = False
with open(input_file) as f:
    for line in f:
        line = line[:-1]
        if not line:
            in_tile = False
            continue
        if not in_tile:
            in_tile = True
            n = int(re.search(r'\d+', line).group())
            tiles[n] = []
        else:
            tiles[n].append([int(c == '#') for c in line])
n_tiles = len(tiles.keys())
board_len = int(n_tiles ** .5)
tile_len = len(line)
print(f'Tiles: {n_tiles}, Board {board_len}x{board_len}')

def conv(edges):
    return tuple(int(edge, 2) for edge in edges)

def rotate(edges):
    right, left, top, bottom = edges
    top, bottom = top[::-1], bottom[::-1]
    return (top, bottom, left, right)

def x_flip(edges):
    top, bottom, right, left = edges
    top, bottom = top[::-1], bottom[::-1]
    return (top, bottom, left, right)

def y_flip(edges):
    bottom, top, left, right = edges
    left, right = left[::-1], right[::-1]
    return (top, bottom, left, right)

def get_edges(tile):
    top = ''.join(map(str, tile[0]))
    bottom = ''.join(map(str, tile[-1]))
    l_v = [str(r[0]) for r in tile]
    left = ''.join(l_v)
    r_v = [str(r[-1]) for r in tile]
    right = ''.join(r_v)
    return (top, bottom, left, right)

def all_comb(edges):
    s = set()
    r_edges = edges
    for rot in range(4):
        r_edges = rotate(r_edges)
        s.add(conv(r_edges))
        s.add(conv(x_flip(r_edges)))
        s.add(conv(y_flip(r_edges)))
        s.add(conv(x_flip(y_flip(r_edges))))
    return s

edge_map = {
    (0, -1): 0,
    (0, 1): 1,
    (-1, 0): 2,
    (1, 0): 3,
}

def fits(board, edges, nx, ny):
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        cx, cy = nx + dx, ny + dy
        if board.get((cx, cy)):
            n_edge = edge_map[dx, dy]
            e_edge = {0: 1, 1: 0, 2: 3, 3: 2}[n_edge]
            if edges[n_edge] != board[cx, cy][1][e_edge]:
                return False
    return True

def add(o_board, o_tiles, n, edges, x, y):
    board = deepcopy(o_board)
    tiles = deepcopy(o_tiles)
    board[x, y] = [n, edges]
    tiles.pop(n)
    if len(tiles.keys()) == 0:
        return True, board
    for num, tile in tiles.items():
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = x + dx, y + dy
            if nx not in range(board_len) or ny not in range(board_len) or board.get((nx, ny)):
                continue # illegal or filled space
            for t_edges in all_comb(get_edges(tile)):
                if fits(board, t_edges, nx, ny):
                    valid, board = add(board, tiles, num, t_edges, nx, ny)
                    if valid:
                        return True, board
    return False, board

def print_tile(tile):
    for row in tile:
        print(''.join(map(str, row)))

# test
tile = tiles[list(tiles.keys())[0]]
edges = get_edges(tile)
assert edges == x_flip(x_flip(edges)) # prove associative
assert edges == y_flip(y_flip(edges)) # see above
assert x_flip(y_flip(edges)) == y_flip(x_flip(edges)) # prove commutative
assert edges == rotate(rotate(rotate(rotate(edges)))) # 4 rotations == no change
# end test

for n, tile in tiles.items():
    print('Tile:', n)
    for edges in all_comb(get_edges(tile)):
        valid, board = add({}, tiles, n, edges, 0, 0)
        if valid:
            break
        if len(board.keys()) == board_len ** 2:
            break
    else:
        continue
    break

if not valid:
    print("Something's wrong; couldn't solve")

for y in {0, board_len - 1}:
    for x in {0, board_len - 1}:
        p1 *= board[x, y][0]
print(f'Part 1: {p1}')


print(f'Part 2: {p2}')
