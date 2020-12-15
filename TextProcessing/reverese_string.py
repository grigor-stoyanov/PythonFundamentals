text = input()
reverse_text = ''
while not text == 'end':
    reverse_text = text[::-1]
    print(f'{text} = {reverse_text}')
    text = input()
