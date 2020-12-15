def move(text, letters):
    to_move = text[:letters:]
    text = text.replace(to_move, '', 1)
    text = text + to_move
    return text


def insert(text, i, to_insert):
    text = text[:i:] + to_insert + text[i::]
    return text


encrypted_msg = input()
command = input()
while not command == 'Decode':
    command = command.split('|')
    if command[0] == 'Move':
        num_letters = int(command[1])
        encrypted_msg = move(encrypted_msg, num_letters)
    elif command[0] == 'Insert':
        index, value = command[1:]
        encrypted_msg = insert(encrypted_msg, int(index), value)
    elif command[0] == 'ChangeAll':
        substring, replacement = command[1:]
        encrypted_msg = encrypted_msg.replace(substring, replacement)
    command = input()
print(f'The decrypted message is: {encrypted_msg}')