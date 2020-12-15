def palindrome(list_of_integers):
    array = list_of_integers.split(", ")
    for each in range(0, len(array)):
        current_number = array[each]
        if len(current_number) % 2 == 1:
            half = current_number[:len(current_number)//2]
            reversed_half = current_number[:len(current_number)//2:-1]
            if half == reversed_half:
                print(True)
            else:
                print(False)
        else:
            half = current_number[:len(current_number) // 2]
            reversed_half = current_number[:(len(current_number)//2)-1:-1]
            if half == reversed_half:
                print(True)
            else:
                print(False)


palindrome(input())