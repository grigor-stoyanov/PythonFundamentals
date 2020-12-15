import re

line = input()
validation = r'(^>>)(?P<name>\w+)<<(?P<price>\d+(\.?\d+)?)!(?P<quantity>\d+)($|\s)'
furniture = []
total_cost = 0
while not line == 'Purchase':
    match = re.search(validation, line)
    if match:
        furniture.append(match.group('name'))
        total_cost += float(match.group('price')) * int(match.group('quantity'))
    line = input()
print('Bought furniture:')
print('\n'.join(furniture))
print(f'Total money spend: {total_cost:.2f}')
