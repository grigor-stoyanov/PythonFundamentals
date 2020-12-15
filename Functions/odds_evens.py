def sum_odds_evens(a):
    sum_odds = 0
    sum_evens = 0
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) % 2 == 1:
            sum_odds += int(a[i])
        else:
            sum_evens += int(a[i])
    return sum_odds, sum_evens


number = input()
print(f'Odd sum = {sum_odds_evens(number)[0]}, Even sum = {sum_odds_evens(number)[1]}')