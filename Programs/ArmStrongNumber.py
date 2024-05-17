def is_armstrong_number(number):
    temp = number
    digit = 0
    length = len(str(number))
    while temp > 0:
        digit += (temp % 10) ** length
        temp //= 10

    if number == digit:
        return True
    return False


print(is_armstrong_number(15468))

