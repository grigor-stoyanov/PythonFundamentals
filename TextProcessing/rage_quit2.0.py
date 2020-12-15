line = input().upper()
result = ''
current_result = ''
index = 0
while index < len(line):
    if not line[index].isdigit():
        current_result += line[index]
        index += 1
    else:
        number = ''
        while line[index].isdigit():
            number += line[index]
            index += 1
            if index >= len(line):
                break
        number = int(number)
        current_result = current_result*number
        result += current_result
        current_result = ''
print(f'Unique symbols used: {len(set(result))}')
print(f'{result}')