# Given an integer x, return true if x is a palindrome, and false otherwise.

def is_palindrome(x):
    temp = abs(x)
    result = 0
    while temp > 0:
        result = result*10 + temp%10
        temp = temp//10
    
    return result == x



x = 121
print(is_palindrome(x))
x = -121
print(is_palindrome(x))
x = 10
print(is_palindrome(x))
x = -101
print(is_palindrome(x)) 
x = 12321
print(is_palindrome(x))
x = 123321
print(is_palindrome(x))
x = 0
print(is_palindrome(x))