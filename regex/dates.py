# import re
#
# regex = r'\d{2}([/.\-])[A-Z][a-z]{2}\1\d{4}'
# text = input()
# matches = re.finditer(regex, text)
# for date in matches:
#     m_obj = date.group(0)
#     day = m_obj[0:2]
#     month = m_obj[3:6]
#     year = m_obj[7:11]
#     print(f'Day: {day}, Month: {month}, Year: {year}')
import re

regex = r'(?P<day>\d{2})(?P<separator>[/.\-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'
text = input()
matches = re.finditer(regex, text)
for date in matches:
    d = date.groupdict()
    print(f'Day: {d["day"]}, Month: {d["month"]}, Year: {d["year"]}')
