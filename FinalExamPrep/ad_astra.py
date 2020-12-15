import re

regex = r'(#|\|)(?P<name>[a-zA-Z\s]+)\1(?P<date>(\d{2}\/){2}\d{2})\1(?P<cal>[1-9][0-9]{0,5}|0)\1'
food = input()
total_calories = 0
food_dict = {}
matches = re.finditer(regex, food)
for match in matches:
    food_dict[match] = match.groupdict()
    total_calories += int(food_dict[match]['cal'])
print(f"You have food to last you for: {total_calories // 2000} days!")
for key in food_dict:
    print(f"Item: {food_dict[key]['name']}, Best before: {food_dict[key]['date']}, Nutrition: {food_dict[key]['cal']}")
