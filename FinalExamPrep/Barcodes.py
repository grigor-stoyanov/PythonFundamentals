import re


n = int(input())
regex = r'@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+'
for _ in range(0, n):
    barcode = input()
    if re.search(regex, barcode):
        group = re.findall(r'\d+', barcode)
        if group:
            print(f'Product group: {"".join(group)}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')