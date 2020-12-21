#!/usr/bin/env python3

import re
import sys

from copy import deepcopy

test = len(sys.argv) > 1 and sys.argv[1] == 'test'
pretty = len(sys.argv) > 2
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
print(f'Tiles: {n_tiles}, Board: {board_len}x{board_len}')

def convert_edge(edges):
    return tuple(int(edge, 2) for edge in edges)

def edge_rotate(top, bottom, left, right):
    return (left[::-1], right[::-1], bottom, top)

def edge_xflip(top, bottom, left, right):
    return (top[::-1], bottom[::-1], right, left)

def edge_yflip(top, bottom, left, right):
    return (bottom, top, left[::-1], right[::-1])

def get_edges(tile):
    top = ''.join(map(str, tile[0]))
    bottom = ''.join(map(str, tile[-1]))
    left = ''.join([str(r[0]) for r in tile])
    right = ''.join([str(r[-1]) for r in tile])
    return (top, bottom, left, right)

def all_edge_combinations(edges):
    s = set()
    r_edges = edges
    for rot in range(4):
        r_edges = edge_rotate(*r_edges)
        s.add(convert_edge(r_edges))
        s.add(convert_edge(edge_xflip(*r_edges)))
        s.add(convert_edge(edge_yflip(*r_edges)))
        s.add(convert_edge(edge_xflip(*edge_yflip(*r_edges))))
    return s

edge_map = {
    (0, -1): 0,
    (0, 1): 1,
    (-1, 0): 2,
    (1, 0): 3,
}

edge_pairs = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

def fits(board, edges, nx, ny):
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        cx, cy = nx + dx, ny + dy
        if board.get((cx, cy)):
            new_edge = edge_map[dx, dy]
            matched_edge = edge_pairs[new_edge]
            if edges[new_edge] != board[cx, cy][1][matched_edge]:
                return False
    return True

def add_tile(o_board, o_tiles, n, edges, x, y):
    board = deepcopy(o_board)
    tiles = deepcopy(o_tiles)
    board[x, y] = [n, edges]
    tiles.pop(n)
    for num, tile in tiles.items():
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = x + dx, y + dy
            if nx not in range(board_len) or ny not in range(board_len) or board.get((nx, ny)):
                continue # illegal or filled space
            for t_edges in all_edge_combinations(get_edges(tile)):
                if fits(board, t_edges, nx, ny):
                    board = add_tile(board, tiles, num, t_edges, nx, ny)
    return board

def print_tile(tile):
    for row in tile:
        print(''.join(map(str, row)))

# test
tile = tiles[list(tiles.keys())[0]]
edges = get_edges(tile)
assert edges == edge_xflip(*edge_xflip(*edges)) == edge_yflip(*edge_yflip(*edges)) # prove 2 flips == no change
assert edge_xflip(*edge_yflip(*edges)) == edge_yflip(*edge_xflip(*edges)) # prove commutative
assert edges == edge_rotate(*edge_rotate(*edge_rotate(*edge_rotate(*edges)))) # 4 rotations == no change
# end test

for n, tile in tiles.items():
    print(f'Checking tile {n}...')
    for edges in all_edge_combinations(get_edges(tile)):
        board = add_tile({}, tiles, n, edges, 0, 0)
        if len(board.keys()) == n_tiles:
            break # all tiles fit
    else:
        continue
    break

for y in {0, board_len - 1}:
    for x in {0, board_len - 1}:
        p1 *= board[x, y][0]
print(f'Part 1: {p1}')

def find_align(num, edges):
    tile = tiles[num]
    t_edges = get_edges(tile)
    for rot in range(4):
        if edges == convert_edge(t_edges):
            return rot, False, False
        t_edges = edge_xflip(*t_edges)
        if edges == convert_edge(t_edges):
            return rot, True, False
        t_edges = edge_yflip(*t_edges)
        if edges == convert_edge(t_edges):
            return rot, True, True
        t_edges = edge_xflip(*t_edges)
        if edges == convert_edge(t_edges):
            return rot, False, True
        t_edges = edge_yflip(*t_edges)
        t_edges = edge_rotate(*t_edges)
    print('Apparently illegal')
    assert False

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

def do_yflip(tile):
    return tile[::-1]

def do_xflip(tile):
    for r in range(len(tile)):
        tile[r] = tile[r][::-1]
    return tile

# test
A = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
assert A == do_xflip(do_xflip(A))
assert A == do_yflip(do_yflip(A))
assert do_rotate(A) == do_rotate(do_rotate(do_rotate(do_rotate(A))))
# end test

OFF = 1 if pretty else -2 # if set to 1, prints with gaps but other ops fail
pretty_off = 0 if pretty else 1
combined = [[None] * board_len * (tile_len + OFF) for _ in range(board_len * (tile_len + OFF))]
for (y, x), (num, edges) in board.items():
    rot, xf, yf = find_align(num, edges)
    new = tiles[num]
    for r in range(rot):
        new = do_rotate(new)
    if xf:
        new = do_xflip(new)
    if yf:
        new = do_yflip(new)

    chunk_start_x = x * (tile_len + OFF)
    chunk_start_y = y * (tile_len + OFF)
    for dx in range(pretty_off, tile_len - pretty_off):
        for dy in range(pretty_off, tile_len - pretty_off):
            nx = chunk_start_x + dx - pretty_off
            ny = chunk_start_y + dy - pretty_off
            combined[nx][ny] = new[dx][dy]

image = []
for line in combined:
    image.append([])
    for c in line:
        image[-1].append({1: '#', 0: '.' if pretty else ' '}.get(c, ' '))
if pretty:
    print_tile(image)
    sys.exit(0)

top = r'..................#.'
mid = r'#....##....##....###'
bot = r'.#..#..#..#..#..#...'

def search(image):
    found = 0
    for i, line in enumerate(image[1:-1]):
        for c in range(len(line) - len(mid)):
            if re.match(mid, ''.join(line[c:])) and re.match(top, ''.join(image[i][c:])) and re.match(bot, ''.join(image[i + 2][c:])):
                found += 1
    return found

for i in range(16):
    if i % 8 == 0:
        image = do_xflip(image)
    if i % 4 == 0:
        image = do_yflip(image)
    if i % 2 == 0:
        image = do_rotate(image)

    found = search(image)
    if found:
        break

for line in image:
    p2 += line.count('#')
p2 -= found * sum((x.count('#') for x in {top, mid, bot}))
print(f'Part 2: {p2}')
