def add_user(forces_dic, user, side):
    if not any(user in value for key, value in forces_dic.items()):
        if side not in forces_dic:
            forces_dic[side] = []
            forces_dic[side].append(user)
        elif user not in forces_dic[side]:
            forces_dic[side].append(user)
    return forces_dic


def transfer_user(forces_dic, user, side):
    filtered_users = {key: value for key, value in forces_dic.items() if user not in value}
    if not filtered_users == forces_dic:
        forces_dic = filtered_users
        forces_dic = add_user(forces_dic, user, side)
    else:
        forces_dic = add_user(forces_dic, user, side)
    print(f'{user} joins the {side} side!')
    return forces_dic


cmd = input()
forces = {}

while not cmd == 'Lumpawaroo':
    cmd_list = cmd.split(' | ')
    if len(cmd_list) > 1:
        force_side, force_user = cmd.split(' | ')
        forces = add_user(forces, force_user, force_side)
    else:
        force_user, force_side = cmd.split(' -> ')
        forces = transfer_user(forces, force_user, force_side)
    cmd = input()

forces = dict(sorted(forces.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in forces.items():
    value.sort()
    if value:
        print(f'Side: {key}, Members: {len(value)}')
        print('! '+'! '.join(value))
