sugar_cubes = input().split()
command = input().split()
index = 0
while not command[0] == 'Mort':
    if command[0] == 'Add':
        sugar_cubes.append(command[1])
    elif command[0] == 'Remove':
        sugar_cubes.remove(command[1])
    elif command[0] == 'Replace':
        for i in range(0, len(sugar_cubes)):
            if sugar_cubes[i] == command[1]:
                index = i
                sugar_cubes.pop(i)
                sugar_cubes.insert(i, command[2])
                break
    elif command[0] == 'Collapse':
        sugar_cubes = [ele for ele in sugar_cubes if int(ele) >= int(command[1])]
    command = input().split()
print(' '.join(sugar_cubes))
