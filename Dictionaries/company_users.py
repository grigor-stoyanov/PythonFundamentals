cmd = input()
company_dict = {}
while not cmd == 'End':
    companyName, employeeId = cmd.split(' -> ')
    if companyName not in company_dict:
        company_dict[companyName] = [employeeId]
    else:
        if employeeId not in company_dict[companyName]:
            company_dict[companyName].append(employeeId)
    cmd = input()
company_dict = dict(sorted(company_dict.items(), key=lambda x: x[0]))
for key, value in company_dict.items():
    print(key)
    print('-- '+'\n-- '.join(value))