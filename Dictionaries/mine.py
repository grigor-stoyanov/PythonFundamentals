cmd = input()
mined = {}
while not cmd == 'stop':
    key = cmd
    cmd = input()
    value = int(cmd)
    if key not in mined:
        mined[key] = value
    else:
        mined[key] += value
    cmd = input()
for key, value in mined.items():
    print(f'{key} -> {value}')