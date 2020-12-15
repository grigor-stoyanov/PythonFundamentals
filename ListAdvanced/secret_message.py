def decode(text):
    letters = list(text)
    if len(letters) > 2:
        first_letter = [letter for letter in letters if '0' <= letter <= '9']
        letters = [letter for letter in letters if not letter in first_letter]
        first_letter = chr(int(''.join(first_letter)))
        letters.insert(0, first_letter)
        letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


message = input().split()
message = [decode(word) for word in message]
message = ' '.join(message)
print(message)