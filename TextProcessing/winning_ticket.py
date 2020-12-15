WINNING_SYMBOLS = ['@', '#', '$', '^']


def is_jackpot(ticket):
    left = ticket[:10]
    right = ticket[10:20]
    if not left == right:
        return False
    else:
        for symbol in WINNING_SYMBOLS:
            if ticket.count(symbol) == 20:
                return True
    return False


def is_winning(ticket):
    left = ticket[:10]
    right = ticket[10:20]
    for symbol in WINNING_SYMBOLS:
        if symbol*6 in left and symbol*6 in right:
            return True
    return False


line = input().split(', ')
for ticket in line:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print('invalid ticket')
        continue
    elif is_jackpot(ticket):
        for symbol in WINNING_SYMBOLS:
            if symbol in ticket:
                print(f"ticket \"{ticket}\" - 10{symbol} Jackpot!")
                break
        continue
    elif is_winning(ticket):
        left = ticket[:10]
        right = ticket[10:20]
        for symbol in WINNING_SYMBOLS:
            if left.count(symbol) >= 6 and right.count(symbol) >= 6:
                match_length = min([left.count(symbol), right.count(symbol)])
                print(f"ticket \"{ticket}\" - {match_length}{symbol}")
                break
        continue
    else:
        print(f"ticket \"{ticket}\" - no match")
