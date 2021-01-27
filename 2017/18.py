#!/usr/bin/env python3

import sys
import threading

from queue import Queue, Empty

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    cmds = utils.load_split_lines(f)

def run(put_q, get_q, end, send_count, ID):
    ip = 0
    regs = {'p': ID}
    recovered = None
    while ip in range(len(cmds)):
        cmd = cmds[ip]
        op = cmd[0]
        if op == 'snd':
            try:
                sound = int(cmd[1])
            except ValueError:
                sound = regs.get(cmd[1], 0)
            if put_q.full():
                put_q.get()
            put_q.put(sound)
            if send_count is not None:
                send_count.v += 1
        elif op == 'set':
            x = cmd[1]
            try:
                y = int(cmd[2])
            except ValueError:
                y = regs[cmd[2]]
            regs[x] = y
        elif op == 'add':
            x = cmd[1]
            try:
                y = int(cmd[2])
            except:
                y = regs[cmd[2]]
            regs[x] = regs.get(x, 0) + y
        elif op == 'mul':
            x = cmd[1]
            try:
                y = int(cmd[2])
            except ValueError:
                y = regs[cmd[2]]
            regs[x] = regs.get(x, 0) * y
        elif op == 'mod':
            x = cmd[1]
            try:
                y = int(cmd[2])
            except ValueError:
                y = regs[cmd[2]]
            regs[x] = regs.get(x, 0) % y
        elif op == 'rcv':
            if end:
                try:
                    x = int(cmd[1])
                except ValueError:
                    x = regs.get(cmd[1], 0)
                if x != 0:
                    recovered = get_q.get()
                    return recovered
            else:
                try:
                    recovered = get_q.get(timeout=1)
                    x = cmd[1]
                    regs[x] = recovered
                except Empty:
                    return recovered
        elif op == 'jgz':
            try:
                x = int(cmd[1])
            except:
                x = regs.get(cmd[1], 0)
            if x > 0:
                try:
                    ip += int(cmd[2])
                except:
                    ip += regs[cmd[2]]
                continue
        ip += 1
    return recovered

q = Queue(maxsize=1)
p1 = run(q, q, True, None, 0)
print(f'Part 1: {p1}')

class Integer:
    def __init__(self):
        self.v = 0

p2 = Integer()

q0 = Queue()
q1 = Queue()

r0 = threading.Thread(target=run, args=(q0, q1, False, None, 0))
r1 = threading.Thread(target=run, args=(q1, q0, False, p2, 1))

r0.start()
r1.start()

r0.join()
r1.join()

print(f'Part 2: {p2.v}')
