line = input()
extension = ''
name = ''
for i in range(-1, -len(line), -1):
    if line[i] in '.':
        extension = line[i+1::]
        mark = i
        break
for i in range(mark, -len(line),-1):
    if line[i] in "\\":
        name = line[i+1:mark:]
        break
print(f'File name: {name}')
print(f'File extension: {extension}')