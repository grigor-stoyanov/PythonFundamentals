num_students = int(input())
grade_book = {}
for _ in range(0, num_students):
    student = input()
    grade = float(input())
    if student not in grade_book:
        grade_book[student] = [grade]
    else:
        grade_book[student].append(grade)
grade_book = {key: sum(value)/len(value) for key, value in grade_book.items() if (sum(value)/len(value)) >= 4.50}
grade_book = dict(sorted(grade_book.items(), reverse=True,key=lambda x: x[1]))
for key, value in grade_book.items():
    print(f'{key} -> {value:0.2f}')
