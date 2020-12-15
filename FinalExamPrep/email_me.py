email = input()
user, domain = email.split('@')
sum_domain = 0
sum_user = 0
for acii in domain:
    sum_domain += ord(acii)
for ascii in user:
    sum_user += ord(ascii)
if sum_domain - sum_user <= 0:
    print('Call her!')
else:
    print('She is not the one.')