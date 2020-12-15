def load(percentage):
    bar = ''
    for i in range(1, 11):
        if i <= (percentage // 10):
            bar += '%'
        else:
            bar += '.'
    return bar


progress = int(input())
if not progress == 100:
    print(f'{(progress // 10)*10}% [' + load(progress) + ']')
    print('Still loading...')
else:
    print('100% Complete!')
    print('[' + load(progress) + ']')