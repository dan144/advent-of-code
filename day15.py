#!/usr/bin/python3

import json
import sys

print('Running:',sys.argv[0])

testing = len(sys.argv) == 2

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)

if testing:
    print('TESTING')
    input_file = 'test' + input_file

print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    if testing:
        test_vals = json.loads(f.readline())
        part_one = test_vals['part_one']
        part_two = test_vals['part_two']
    for line in f:
        inputs.append(data_type(line[:-1]))
if testing:
    print(inputs)

print()
print('PART ONE')
ans = None

HP = 200
AP = 3
class Goblin():
    def __init__(self, x, y):
        self.hp = HP
        self.m = 0
        self.x = x
        self.y = y
    def __str__(self):
        return 'G'
class Elf():
    def __init__(self, x, y):
        self.hp = HP
        self.m = 0
        self.x = x
        self.y = y
    def __str__(self):
        return 'E'

goblins = []
elves = []
board = []
for y in range(len(inputs)):
    line = inputs[y]
    board.append([])
    for x in range(len(line)):
        c = line[x]
        if c in '.#':
            board[-1].append(c)
        elif c == 'G':
            g = Goblin(x, y)
            board[-1].append(g)
            goblins.append(g)
        elif c == 'E':
            e = Elf(x, y)
            board[-1].append(e)
            elves.append(e)

def reset_dboard():
    global board
    dboard = []
    for y in range(len(board)):
        dboard.append([])
        for x in range(len(board[0])):
            dboard[-1].append(None if str(board[y][x]) in 'EG#' else 0)
    return dboard

def show_board(show=False):
    if not show:
        return
    global board
    for line in board:
        print(''.join(map(str, line)))
    input()

show_board()

rounds = 0
while len(elves) and len(goblins):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if type(board[y][x]) in {Goblin, Elf} and board[y][x].m == rounds:
                # identify all targets and "in range" points (?)
                target_locs = []
                target_array = goblins if type(board[y][x]) == Elf else elves
                dont = False
                for target in target_array:
                    tx = target.x
                    ty = target.y
                    for xoff, yoff in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
                        if board[ty+yoff][tx+xoff] == '.':
                            target_locs.append((tx+xoff, ty+yoff))
                            board[ty+yoff][tx+xoff] = '?'
                        if x == tx + xoff and y == ty + yoff:
                            dont = True
                            break
                    else:
                        continue
                    break
                show_board()

                # don't move if there's an enemy right next to you
                if dont:
                    for lx, ly in target_locs:
                        board[ly][lx] = '.'
                    board[y][x].m = rounds + 1
                    continue

                # don't move if there's no target locations
                if not target_locs:
                    board[y][x].m = rounds + 1
                    continue

                # find distance to all reachable points (@)
                dboard = reset_dboard()
                points = [(x, y)]
                d = 0
                min_d = None
                while points:
                    npoints = []
                    for point in points:
                        px, py = point
                        if d > 0:
                            dboard[py][px] = d
                            if str(board[py][px]) == '?':
                                board[py][px] = '@'

                        for xoff, yoff in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
                            if not dboard[py+yoff][px+xoff] and str(board[py+yoff][px+xoff]) in '.?' and not (x == px + xoff and y == py + yoff):
                                npoints.append((px+xoff, py+yoff))
                    points = npoints
                    d += 1
                show_board()

                # narrow scope to all nearest points (!)
                for lx, ly in target_locs:
                    d = dboard[ly][lx]
                    if d == 0 or d is None:
                        continue
                    if min_d is None or d in range(1, min_d):
                       min_d = d

                closest_locs = []
                for lx, ly in target_locs:
                    if dboard[ly][lx] == min_d:
                        board[ly][lx] = str(dboard[ly][lx])
                        closest_locs.append((lx, ly))
                    else:
                        board[ly][lx] = '.'
                show_board()

                # choose the point
                min_y = min(closest_locs, key=lambda x: x[1])[1]
                chosen = sorted((list(filter(lambda x: x[1] == min_y, closest_locs))))[0]
                for lx, ly in closest_locs:
                    if (lx, ly) == chosen:
                        board[ly][lx] = '+'
                    else:
                        board[ly][lx] = '.'
                show_board()
                board[chosen[1]][chosen[0]] = '.'  # clean the board up

                # find a path to that point
                dboard = reset_dboard()
                points = [chosen]
                d = 0
                while points:
                    npoints = []
                    for point in points:
                        px, py = point
                        if d > 0:
                            dboard[py][px] = d
                            if str(board[py][px]) == '?':
                                board[py][px] = '@'

                        for xoff, yoff in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
                            if not dboard[py+yoff][px+xoff] and str(board[py+yoff][px+xoff]) in '.?' and not (x == px + xoff and y == py + yoff):
                                npoints.append((px+xoff, py+yoff))
                    points = npoints
                    d += 1
                    if (x, y) in points:
                        break

                # find all moves that minimize distance
                min_d = None
                moves = []
                for xoff, yoff in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
                    d = dboard[y+yoff][x+xoff]
                    if d is None or d == 0:
                        continue
                    if min_d is None or d < min_d:
                        min_d = d
                        moves = [(x+xoff, y+yoff)]
                    elif d == min_d:
                        moves.append((x+xoff, y+yoff))

                # determine if this one can move
                if len(moves) == 0:
                    continue

                # choose first move in that read
                min_y = min(moves, key=lambda x: x[1])[1]
                chosen_move = sorted((list(filter(lambda x: x[1] == min_y, moves))))[0]

                # move the person
                cx = chosen_move[0]
                cy = chosen_move[1]
                me = board[y][x]

                me.x = cx
                me.y = cy
                me.m = rounds + 1
                board[cy][cx] = me
                board[y][x] = '.'

    rounds += 1
    show_board(show=True)

print(rounds)
show_board(show=True)
print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')


print()
print('PART TWO')
ans = None



print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
