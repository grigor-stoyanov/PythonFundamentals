def alphabetical_upper(letter):
    return ord(letter) - 64


def alphabetical_lower(letter):
    return ord(letter) - 96


text = input().split()
result = 0
for ele in text:
    first = ele[0]
    last = ele[-1]
    num = float(ele[1:len(ele) - 1:])
    if first.isupper():
        num = num / alphabetical_upper(first)
    elif first.islower():
        num = num * alphabetical_lower(first)
    if last.isupper():
        num = num - alphabetical_upper(last)
    elif last.islower():
        num = num + alphabetical_lower(last)
    result += num
print(f'{result:0.2f}')
