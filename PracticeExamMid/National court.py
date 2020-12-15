first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
clients = int(input())
hours = 0
while clients > 0:
    hours += 1
    if not hours % 4 == 0:
        clients_per_hour = first_employee+second_employee+third_employee
        clients -= clients_per_hour
print(f'Time needed: {hours}h.')