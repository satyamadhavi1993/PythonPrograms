
def check_any(numbers):
    if any(number % 2 == 0 for number in numbers):
        print("Contains even numbers")
    else:
        print("Does not contain even numbers")


def check_all(numbers):
    if all(number % 2 != 0 for number in numbers):
        print("All numbers are odd numbers")
    else:
        print("Not all numbers are odd numbers")


numbers = [5, 6, 7, 8, 9, 10]
check_any(numbers)
check_all(numbers)

numbers = [5, 7, 9, 11, 13, 15]
check_any(numbers)
check_all(numbers)
