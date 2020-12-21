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
                    board = add(board, tiles, num, t_edges, nx, ny)
    return board

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

if test:
    for n, tile in tiles.items():
        print('Tile:', n)
        for edges in all_comb(get_edges(tile)):
            board = add({}, tiles, n, edges, 0, 0)
            if len(board.keys()) == board_len ** 2:
                break # all tiles fit
        else:
            continue
        break

if not test:
    # board from part 1 to save time
    board = {(0, 0): [3433, (2, 907, 379, 217)], (0, 1): [2837, (907, 320, 926, 560)], (0, 2): [3613, (320, 768, 263, 502)], (1, 2): [1667, (339, 308, 502, 802)], (1, 3): [3853, (308, 842, 119, 66)], (1, 4): [3559, (842, 547, 569, 81)], (1, 5): [1559, (547, 42, 984, 700)], (0, 5): [1811, (255, 194, 292, 984)], (0, 6): [2671, (194, 913, 189, 223)], (0, 7): [3301, (913, 628, 823, 812)], (1, 7): [3169, (726, 26, 812, 198)], (2, 7): [3529, (128, 486, 198, 470)], (2, 8): [2447, (486, 316, 498, 476)], (2, 9): [1109, (316, 464, 214, 356)], (1, 9): [2281, (996, 804, 911, 214)], (1, 10): [1307, (804, 557, 811, 29)], (1, 11): [3943, (557, 690, 1007, 868)], (0, 11): [3833, (997, 285, 864, 1007)], (0, 10): [1013, (1005, 997, 733, 811)], (0, 9): [1213, (687, 1005, 535, 911)], (0, 8): [3881, (628, 687, 807, 389)], (1, 8): [2707, (26, 996, 389, 498)], (2, 11): [2917, (877, 62, 868, 684)], (3, 11): [2791, (836, 286, 684, 270)], (3, 10): [1151, (407, 836, 305, 784)], (3, 9): [2521, (329, 407, 356, 759)], (4, 9): [2659, (815, 678, 759, 636)], (4, 10): [2719, (678, 444, 784, 350)], (4, 11): [1693, (444, 172, 270, 384)], (5, 11): [1051, (201, 460, 384, 672)], (6, 11): [1367, (515, 40, 672, 798)], (6, 10): [2063, (960, 515, 593, 37)], (7, 10): [3877, (481, 800, 37, 916)], (7, 9): [3947, (145, 481, 124, 881)], (7, 8): [2221, (43, 145, 52, 857)], (6, 8): [3583, (820, 998, 627, 52)], (6, 7): [3019, (791, 820, 559, 796)], (7, 7): [2053, (844, 43, 796, 123)], (7, 6): [1181, (14, 844, 101, 34)], (6, 6): [1979, (686, 791, 699, 101)], (6, 5): [2161, (121, 686, 501, 818)], (5, 5): [3359, (70, 899, 181, 501)], (4, 5): [2683, (828, 757, 665, 181)], (3, 5): [2081, (729, 411, 938, 665)], (3, 6): [2477, (411, 116, 84, 536)], (4, 6): [1097, (757, 112, 536, 858)], (4, 7): [2939, (112, 512, 225, 410)], (5, 7): [2351, (441, 445, 410, 559)], (5, 6): [3079, (899, 441, 858, 699)], (5, 8): [2339, (445, 709, 353, 627)], (4, 8): [2531, (512, 815, 595, 353)], (3, 8): [2963, (257, 329, 476, 595)], (3, 7): [3217, (116, 257, 470, 225)], (5, 9): [1103, (709, 303, 636, 795)], (5, 10): [3119, (303, 201, 350, 593)], (6, 9): [2633, (998, 960, 795, 124)], (2, 6): [3257, (312, 128, 140, 84)], (1, 6): [3769, (42, 726, 223, 140)], (2, 5): [3617, (863, 312, 700, 938)], (2, 4): [1889, (226, 863, 81, 321)], (2, 3): [1423, (228, 226, 66, 136)], (2, 2): [2273, (829, 228, 802, 976)], (2, 1): [1087, (703, 829, 643, 999)], (1, 1): [3307, (779, 339, 560, 643)], (1, 0): [1973, (458, 779, 217, 499)], (2, 0): [3319, (107, 703, 499, 669)], (3, 0): [2749, (787, 648, 669, 640)], (4, 0): [2801, (667, 105, 640, 935)], (5, 0): [3083, (617, 923, 935, 615)], (6, 0): [1451, (599, 910, 615, 666)], (6, 1): [1901, (910, 110, 892, 404)], (7, 1): [1447, (454, 231, 404, 489)], (8, 1): [1753, (144, 543, 489, 85)], (8, 0): [1867, (526, 144, 570, 418)], (9, 0): [3767, (371, 158, 418, 1006)], (9, 1): [2731, (158, 724, 85, 186)], (9, 2): [1789, (724, 730, 989, 8)], (9, 3): [3701, (730, 141, 532, 431)], (9, 4): [2857, (141, 732, 409, 682)], (8, 4): [1223, (280, 963, 153, 409)], (8, 3): [1723, (933, 280, 806, 532)], (7, 3): [1381, (531, 108, 792, 806)], (6, 3): [2207, (421, 302, 342, 792)], (6, 2): [1289, (110, 421, 30, 459)], (7, 2): [2693, (231, 531, 459, 589)], (8, 2): [1847, (543, 933, 589, 989)], (5, 2): [3607, (882, 368, 884, 30)], (4, 2): [1873, (385, 770, 311, 884)], (4, 3): [1471, (770, 370, 840, 374)], (5, 3): [1009, (368, 432, 374, 342)], (5, 4): [3691, (432, 70, 162, 138)], (4, 4): [3517, (370, 828, 135, 162)], (3, 4): [1999, (76, 729, 321, 135)], (3, 3): [1949, (61, 76, 136, 840)], (3, 2): [2579, (972, 61, 976, 311)], (3, 1): [3821, (648, 972, 999, 224)], (4, 1): [2833, (105, 385, 224, 827)], (5, 1): [1091, (923, 882, 827, 892)], (6, 4): [1709, (302, 121, 138, 209)], (7, 4): [2371, (108, 889, 209, 153)], (7, 5): [2137, (889, 14, 818, 914)], (8, 5): [1511, (963, 281, 914, 727)], (8, 6): [2909, (281, 221, 34, 563)], (9, 6): [1579, (602, 704, 563, 376)], (10, 6): [2269, (115, 148, 376, 772)], (10, 5): [1409, (220, 115, 288, 399)], (11, 5): [2003, (240, 988, 399, 32)], (11, 6): [2399, (988, 468, 772, 100)], (11, 7): [2099, (468, 439, 492, 301)], (10, 7): [1291, (148, 834, 151, 492)], (9, 7): [2089, (704, 965, 611, 151)], (9, 8): [1039, (965, 347, 990, 971)], (9, 9): [2143, (347, 647, 71, 533)], (9, 10): [2677, (647, 964, 577, 626)], (9, 11): [3413, (964, 44, 1012, 300)], (10, 11): [1429, (202, 290, 300, 254)], (10, 10): [1063, (859, 202, 626, 580)], (10, 9): [2549, (520, 859, 533, 447)], (10, 8): [2417, (834, 520, 971, 344)], (11, 8): [3109, (439, 511, 344, 641)], (11, 9): [2111, (511, 776, 447, 954)], (11, 10): [1279, (776, 260, 580, 500)], (11, 11): [3001, (260, 348, 254, 150)], (8, 11): [2543, (91, 50, 134, 1012)], (7, 11): [2851, (800, 298, 798, 134)], (8, 10): [1163, (591, 91, 916, 577)], (8, 9): [1231, (598, 591, 881, 71)], (8, 8): [3547, (605, 598, 857, 990)], (8, 7): [2027, (221, 605, 123, 611)], (11, 4): [1997, (406, 240, 88, 12)], (11, 3): [2423, (282, 406, 94, 366)], (11, 2): [2287, (497, 282, 126, 974)], (11, 1): [3793, (265, 497, 362, 1015)], (11, 0): [2011, (351, 265, 230, 573)], (10, 0): [3491, (534, 218, 1006, 230)], (10, 1): [1583, (218, 250, 186, 362)], (10, 2): [1567, (250, 360, 8, 126)], (10, 3): [2957, (360, 546, 431, 94)], (10, 4): [2557, (546, 220, 682, 88)], (9, 5): [2239, (732, 602, 727, 288)], (7, 0): [2843, (821, 454, 666, 570)], (2, 10): [2393, (464, 877, 29, 305)], (0, 4): [3643, (17, 255, 96, 569)], (0, 3): [2411, (768, 17, 808, 119)]}

for y in {0, board_len - 1}:
    for x in {0, board_len - 1}:
        p1 *= board[x, y][0]
print(f'Part 1: {p1}')

def find_rot(num, edges):
    tile = tiles[num]
    t_edges = get_edges(tile)
    for rot in range(4):
        t_edges = rotate(t_edges)
        if edges == conv(t_edges):
            return rot + 1, False, False
        t_edges = x_flip(t_edges)
        if edges == conv(t_edges):
            return rot + 1, True, False
        t_edges = y_flip(t_edges)
        if edges == conv(t_edges):
            return rot + 1, True, True
        t_edges = x_flip(t_edges)
        if edges == conv(t_edges):
            return rot + 1, False, True
        t_edges = y_flip(t_edges)
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

OFF = -2
combined = [[None] * board_len * (tile_len + OFF) for _ in range(board_len * (tile_len + OFF))]
for (y, x), (num, edges) in board.items():
    rot, xf, yf = find_rot(num, edges)
    new = tiles[num]
    for r in range(rot):
        new = do_rotate(new)
    if xf:
        new = do_xflip(new)
    if yf:
        new = do_yflip(new)

    s_x = x * (tile_len + OFF)
    s_y = y * (tile_len + OFF)
    for dx in range(1, tile_len - 1):
        for dy in range(1, tile_len - 1):
            nx, ny = s_x + dx - 1, s_y + dy - 1
            combined[nx][ny] = new[dx][dy]

image = []
for line in combined:
    image.append([])
    for c in line:
        image[-1].append({1: '#', 0: '.' if OFF == 1 else ' '}.get(c, ' '))
assert OFF < 0

top = r'..................#.'
mid = r'#....##....##....###'
bot = r'.#..#..#..#..#..#...'

def search(image):
    found = 0

    v = ''.join(map(str, (c % 10 for c in range(20))))
    for i, line in enumerate(image[1:-1]):
        for c in range(len(line)):
            if re.fullmatch(mid, ''.join(line[c:c+20])):
                if re.fullmatch(top, ''.join(image[i][c:c+20])):
                    if re.fullmatch(bot, ''.join(image[i + 2][c:c+20])):
                        found += 1

    return found

for i in range(4):
    if i in {0, 1}:
        image = do_xflip(image)
    if i in {0, 2}:
        image = do_yflip(image)

    for rot in range(4):
        image = do_rotate(image)
        found = search(image)
        if found:
            break
    if found:
        break

    if i in {0, 1}:
        image = do_xflip(image)
    if i in {0, 2}:
        image = do_yflip(image)

for line in image:
    p2 += line.count('#')
p2 -= found * sum((x.count('#') for x in {top, mid, bot}))
print(f'Part 2: {p2}')
