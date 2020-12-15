n = int(input())
my_pieces = {}
for _ in range(n):
    pieces = input()
    piece, composer, key = pieces.split('|')
    my_pieces[piece] = {composer: key}

command = input()
while not command == 'Stop':
    command = command.split('|')
    if command[0] == 'Add':
        piece, composer, key = command[1:]
        if my_pieces.get(piece):
            print(f"{piece} is already in the collection!")
        else:
            my_pieces[piece] = {composer: key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == 'Remove':
        piece = command[1]
        if my_pieces.get(piece):
            del my_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == 'ChangeKey':
        piece, new_key = command[1:]
        if my_pieces.get(piece):
            for composer in my_pieces[piece]:
                my_pieces[piece].update({composer: new_key})
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
my_pieces = dict(sorted(my_pieces.items(), key=lambda x: (x[0], x[1])))
for piece, value in my_pieces.items():
    print(f"{piece} -> Composer: {list(value.keys())[0]}, Key: {list(value.values())[0]}")