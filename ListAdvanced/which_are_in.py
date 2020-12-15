string1 = input().split(', ')
string2 = input()
are_in = [el for el in string1 if el in string2]
print(sorted(set(are_in),key=are_in.index))