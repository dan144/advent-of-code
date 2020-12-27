def run(cmds, regs):
    ip = 0
    while ip < len(cmds):
        cmd = cmds[ip]
        opcode = cmd[0]
        if opcode == 'cpy':
            try:
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
                ip += int(cmd[2])
                continue
        ip += 1
