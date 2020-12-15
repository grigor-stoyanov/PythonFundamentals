cmd = input()
compete = {}
languages = {}
while not cmd == 'exam finished':
    username, *command = cmd.split('-')
    if len(command) > 1:
        language, points = command
        points = int(points)
        languages[language] = languages.get(language, 0) + 1
        if compete.get(username, True) < points:
            compete.update({username: points})
    elif command[0] == 'banned':
        compete.pop(username)
    cmd = input()
compete = dict(sorted(compete.items(), reverse=False, key=lambda x: (-x[1], x[0])))
languages = dict(sorted(languages.items(), reverse=False, key=lambda x: (-x[1], x[0])))
print('Results:')
for user, point in compete.items():
    print(f'{user} | {point}')
print('Submissions:')
for lang, sub in languages.items():
    print(f'{lang} - {sub}')

