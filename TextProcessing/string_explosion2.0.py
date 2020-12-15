line = input()
strength = 0
index = 0
new_line = ''
while index < len(line):
    if not line[index] in '>':
        new_line += line[index]
    else:
        new_line += '>'
        index += 1
        strength += int(line[index])
        while strength > 0 and not line[index] in '>':
            index += 1
            strength -= 1
            if index >= len(line):
                break
        index -= 1
    index += 1
print(new_line)