def take_odd(pword):
    pword = pword[1::2]
    print(pword)
    return pword


def cut(pword, index, length):
    to_cut = pword[index:index + length:]
    pword = pword.replace(to_cut, '', 1)
    print(pword)
    return pword


def substitute(pword, substring, substitute):
    if substring in pword:
        pword = pword.replace(substring, substitute)
        print(pword)
        return pword
    else:
        print('Nothing to replace!')
        return pword


password = input()
cmd = input()
while not cmd == 'Done':
    cmd = cmd.split()
    if cmd[0] == 'TakeOdd':
        password = take_odd(password)
    elif cmd[0] == 'Cut':
        password = cut(password, int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'Substitute':
        password = substitute(password, cmd[1], cmd[2])
    cmd = input()
print(f'Your password is: {password}')
