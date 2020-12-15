import re

sentence = input().lower()
word = input().lower()
word_count = 0
matches = re.finditer(word+'\\b', sentence, re.IGNORECASE)
for match in matches:
    word_count += 1
print(word_count)
