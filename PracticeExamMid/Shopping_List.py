initial_list = input().split('!')
cmds = input()
while not cmds == 'Go Shopping!':
    cmd = cmds.split()
    if cmd[0] == 'Urgent':
        if initial_list.count(cmd[1]) == 0:
            initial_list.insert(0, cmd[1])

    if cmd[0] == 'Unnecessary':
        if not initial_list.count(cmd[1]) == 0:
            initial_list.remove(cmd[1])
    if cmd[0] == 'Correct':
        if not initial_list.count(cmd[1]) == 0:
            initial_list[initial_list.index(cmd[1])] = cmd[2]

    if cmd[0] == 'Rearrange':
        if not initial_list.count(cmd[1]) == 0:
            initial_list.remove(cmd[1])
            initial_list.append(cmd[1])

    cmds = input()

print(', '.join(initial_list))