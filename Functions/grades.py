def check_grade(grade):
    if 2 <= grade <= 2.99:
        return 'Fail'
    elif 3 <= grade <= 3.49:
        return 'Poor'
    elif 3.5 <= grade <= 4.49:
        return 'Good'
    elif 4.5 <= grade <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade <= 6:
        return 'Excellent'


print(check_grade(float(input())))
