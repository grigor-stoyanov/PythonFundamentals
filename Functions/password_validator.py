def validate(pword):
    cond1 = 6 <= len(pword) <= 10
    if not cond1:
        print("Password must be between 6 and 10 characters")
    cond2 = True
    cond3 = True
    count_digit = 0
    for each_letter in range(0, len(pword)):
        if not pword[each_letter].isdigit():
            if pword[each_letter].isalpha() and cond2:
                continue
            else:
                cond2 = False
        else:
            count_digit += 1
    if not cond2:
        print("Password must consist only of letters and digits")
    if count_digit < 2:
        print("Password must have at least 2 digits")
        cond3 = False
    if cond1 and cond2 and cond3:
        print('Password is valid')


password = input()
validate(password)