cen = int(input())
#36524 days 100 years 1 year 365,24
years = cen*100
days = int(years*365.2422)
hours = days*24
minutes = hours*60
print(f'{cen} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
