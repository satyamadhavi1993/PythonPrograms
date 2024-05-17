def is_palindrome(i):
    number = i
    reverse_number = 0

    while i > 0:
        digit = i % 10
        reverse_number = reverse_number * 10 + digit
        i = i // 10
    if number == reverse_number:
        print(True)
    else:
        print(False)    


is_palindrome(321123)
