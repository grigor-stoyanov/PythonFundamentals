import math

deck = input()
shuffles = int(input())
deck_list = deck.split()
shuffle = []
half1 = []
# slicing half1 = [1:limit]
# half2 = [limit:len(deck_list)]
half2 = []
limit = math.ceil(len(deck_list)/2)
# a 2 3 4 1 swap
# a 3 4 2
# a 2 3 4 5 6 3 swaps
# a 4 3 2 5 6
# a 4 2 3 5 6
# a 4 2 5 3 6
# a 2 3 4 5 6 7 8 4 swaps
# a 5 3 4 2 6 7 8
# a 5 2 4 3 6 7 8
# a 5 2 6 3 4 7 8
# a 5 2 6 3 7 4 8
# a 2 3 4 5 6 7 8 9 10 6 swaps
# a 6 3 4 5 2 7 8 9 10
# a 6 2 4 5 3 7 8 9 10
# a 6 2 7 5 3 4 8 9 10
# a 6 2 7 3 5 4 8 9 10
# a 6 2 7 3 8 4 5 9 10
# a 6 2 7 3 8 4 9 5 10
# a 2 3 4 5 6 7 8 9 10 j q 9 swaps
# a 7 3 4 5 6 2 8 9 10 j q
# a 7 2 4 5 6 3 8 9 10 j q
# a 7 2 8 5 6 3 4 9 10 j q
# a 7 2 8 3 6 5 4 9 10 j q
# a 7 2 8 3 9 5 4 6 10 j q
# a 7 2 8 3 9 4 5 6 10 j q
# a 7 2 8 3 9 4 10 6 5 j q
# a 7 2 8 3 9 4 10 5 6 j q
# a 7 2 8 3 9 4 10 5 j 6 q
for times in range(0,shuffles):
    for index in range(0,limit):
        half1.append(deck_list[index])
    for index in range(limit,len(deck_list)):
        half2.append(deck_list[index])
    for i in range(0,limit):
        shuffle += half1[i]
        shuffle += half2[i]
    deck_list = shuffle
# гледат към едно и също а -> [2 , 3] <- b промени а, b се променя .copy() ги прави нереферентни
    shuffle = []
    half1 = []
    half2 = []
print(deck_list)
# zip([:limit],[limit:]) прави същото
# extend([1,2,[3,4]]) лист от листове