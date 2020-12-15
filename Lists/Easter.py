names = input()
names_list = names.split()
cmd = input()
names_string = ""
while not cmd == "No Money":
    if cmd.split()[0] == "OutOfStock":
        for index in range(len(names_list)):
            if names_list[index] == cmd.split()[1]:
                names_list[index] = None
    if cmd.split()[0] == "Required" and int(cmd.split()[2]) < int(len(names_list)) and int(cmd.split()[2])>0:
        names_list[int(cmd.split()[2])] = cmd.split()[1]
    if cmd.split()[0] == "JustInCase":
        names_list[len(names_list)-1] = cmd.split()[1]
    cmd = input()
for i in range(0, len(names_list)):
    if not names_list[i] is None:
        names_string += f'{names_list[i]} '
print(names_string)