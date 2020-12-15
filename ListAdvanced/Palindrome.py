words = input().split()
searched_word = input()
palindroms = [word for word in words if word == word[::-1]]
print(palindroms)
occ = palindroms.count(searched_word)
print(f'Found palindrome {occ} times')