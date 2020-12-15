num_lines = int(input())
users = {}
for _ in range(0, num_lines):
    cmd = input()
    if 'unregister' not in cmd:
        cmd, user, plate_number = cmd.split()
        if user not in users:
            users[user] = plate_number
            print(f'{user} registered {plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {plate_number}')
    else:
        cmd, user = cmd.split()
        if user not in users:
            print(f'ERROR: user {user} not found')
        else:
            users.pop(user)
            print(f'{user} unregistered successfully')
for key, value in users.items():
    print(f'{key} => {value}')
