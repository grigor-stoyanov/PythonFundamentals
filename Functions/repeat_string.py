def repeat_string(text, n):
    result = ''
    for i in range(0, n):
        result += text
    return result


name = input()
limit = int(input())
print(repeat_string(name, limit))