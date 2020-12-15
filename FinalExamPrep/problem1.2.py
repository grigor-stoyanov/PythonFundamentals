email = input()
command = input()
while not command == 'Complete':
    if 'Make Upper' in command:
        email = email.upper()
        print(email)
    if 'Make Lower' in command:
        email = email.lower()
        print(email)
    if 'GetDomain' in command:
        count = int(command.split()[1])
        print(email[-count::])
    if 'GetUsername' in command:
        if '@' in email:
            print(email.split('@')[0])
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    if 'Replace' in command:
        char = command.split()[1]
        email = email.replace(char, '-')
        print(email)
    if 'Encrypt' in command:
        for symbol in email:
            print(ord(symbol), end=' ')
    command = input()
