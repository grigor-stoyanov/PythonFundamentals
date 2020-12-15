def add_user(users_dic, name, sent_msgs, received_msgs):
    users_dic[name] = users_dic.get(name, {'sent': int(sent_msgs), 'received': int(received_msgs)})
    return users_dic


def send_message(users_dic, sender_name, receiver_name, msgs_capacity):
    if users_dic.get(sender_name) and users_dic.get(receiver_name):
        users_dic[sender_name]['sent'] += 1
        users_dic[receiver_name]['received'] += 1
        users_dic = check_capacity(users_dic, sender_name, msgs_capacity)
        users_dic = check_capacity(users_dic, receiver_name, msgs_capacity)
    return users_dic


def check_capacity(user_dic, name, n):
    if sum(user_dic[name].values()) >= n:
        user_dic.pop(name)
        print(f'{name} reached the capacity!')
    return user_dic


def delete_user(user_dic, name):
    if name == 'All':
        user_dic.clear()
    elif user_dic.get(name):
        user_dic.pop(name)
    return user_dic


capacity = int(input())
users = {}
line = input()
while not line == 'Statistics':
    if 'Add' in line:
        username, sent, received = line.split('=')[1:]
        users = add_user(users, username, sent, received)
    if 'Message' in line:
        sender, receiver = line.split('=')[1:]
        users = send_message(users, sender, receiver, capacity)
    if 'Empty' in line:
        username = line.split('=')[1]
        users = delete_user(users, username)
    line = input()
users = dict(sorted(users.items(), reverse=False, key=lambda x: (-x[1]['received'], x[0])))
print(f'Users count: {len(users)}')
for user, messages in users.items():
    print(f'{user} - {sum(messages.values())}')
