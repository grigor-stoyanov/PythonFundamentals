cmd = input()
courses = {}
while not cmd == 'end':
    courseName, studentName = cmd.split(' : ')
    if courseName not in courses:
        courses[courseName] = [studentName]
    else:
        courses[courseName].append(studentName)
    cmd = input()
courses = dict(sorted(courses.items(), reverse=True, key=lambda x: len(x[1])))
for key, value in courses.items():
    value.sort()
    print(f'{key}: {len(value)}')
    print('-- '+'\n-- '.join(value))


