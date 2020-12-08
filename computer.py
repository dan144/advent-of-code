from copy import deepcopy

def run(cmd, term=True):
    cmd = deepcopy(cmd)
    acc = 0
    ip = 0
    quit = False
    try:
        while True:
            if term and cmd[ip][2]:
                break
            ins = cmd[ip]
            ins[2] = True
            if ins[0] == 'nop':
                ip += 1
            elif ins[0] == 'acc':
                acc += ins[1]
                ip += 1
            elif ins[0] == 'jmp':
                ip += ins[1]
    except IndexError:
        quit = True
    return acc, quit
