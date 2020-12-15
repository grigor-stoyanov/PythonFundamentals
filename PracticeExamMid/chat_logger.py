chat_log = []
command = input().split()
while not command[0] == 'end':
    if command[0] == 'Chat':
        chat_log.append(command[1])
    elif command[0] == 'Delete':
        chat_log.remove(command[1])
    elif command[0] == 'Edit':
        for i in range(0, len(chat_log)):
            if chat_log[i] == command[1]:
                chat_log.pop(i)
                chat_log.insert(i, command[2])
                break
    elif command[0] == 'Pin':
        for i in range(0, len(chat_log)):
            if chat_log[i] == command[1]:
                chat_log.append(chat_log[i])
                chat_log.pop(i)
                break
    elif command[0] == 'Spam':
        command.pop(0)
        for each in command:
            chat_log.append(each)
    command = input().split()
print('\n'.join(chat_log))