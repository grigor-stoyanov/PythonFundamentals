line = input()
strength = 0
index = 0
while index < len(line):
    if line[index] in '>':
        index += 1
        strength += int(line[index])
        while not line[index] in '>' and strength > 0:
            line = line[:index] + line[index+1:]
            strength -= 1
            if index >= len(line):
                break
        index -= 1
    index += 1
print(line)