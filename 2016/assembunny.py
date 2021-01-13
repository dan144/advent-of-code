def run(cmds, regs):
    consecutive = 0
    last_out = None
    ip = 0
    while ip < len(cmds):
        cmd = cmds[ip]
        opcode = cmd[0]
        try:
            if opcode == 'cpy':
                if cmd[2] in regs.keys():
                    try:
                        # try to cast, read reg if not int
                        regs[cmd[2]] = int(cmd[1])
                    except:
                        regs[cmd[2]] = regs[cmd[1]]
            elif opcode == 'inc':
                regs[cmd[1]] += 1
            elif opcode == 'dec':
                regs[cmd[1]] -= 1
            elif opcode == 'jnz':
                try:
                    x = regs[cmd[1]]
                except:
                    x = int(cmd[1])
                if x != 0:
                    try:
                        # try to cast, read reg if not int
                        ip += int(cmd[2])
                    except ValueError:
                        ip += regs[cmd[2]]
                    continue
            elif opcode == 'tgl':
                try:
                    try:
                        # try to cast, read reg if not int
                        x = int(cmd[1])
                    except:
                        x = regs[cmd[1]]
                    x += ip

                    n_arg = len(cmds[x]) - 1
                    if n_arg == 1:
                        cmds[x][0] = {'inc': 'dec'}.get(cmds[x][0], 'inc')
                    elif n_arg == 2:
                        cmds[x][0] = {'jnz': 'cpy'}.get(cmds[x][0], 'jnz')
                except:
                    pass
            elif opcode == 'out':
                try:
                    # try to cast, read reg if not int
                    out = int(cmd[1])
                except:
                    out = regs[cmd[1]]
                if last_out is None or out == abs(last_out - 1):
                    last_out = out
                    consecutive += 1
                    if consecutive > 1000:
                        return True # long enough to assume
                else:
                    return False # pattern broke
        except IndexError:
            # ignore touching commands outside the range
            pass
        ip += 1
