note = input()
todo_list = []
while not note == "End":
    todo_list.append(note.split('-'))
    note = input()
todo_list2 = sorted(todo_list,key = int(todo_list[0][0]))
print(todo_list2)
