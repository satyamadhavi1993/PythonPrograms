def is_palindrome(s):
    s2 = ""
    num_of_iterations = 0
    for i in reversed(s):
        num_of_iterations += 1
        s2 += i
    print(f'Number :: {num_of_iterations}')    
    if s == s2:
        return True
    return False


def is_palindrome2(s):
    left = 0
    right = len(s) - 1
    num_of_iterations = 0
    while left < right:
        num_of_iterations += 1
        if not s[left] == s[right]:
            return False
        else:
            left += 1
            right -= 1
    print(f'Number :: {num_of_iterations}')     
    return True


print(is_palindrome('abcdefghijkllkjihgfedcbaa'))
print(is_palindrome2('abcdefghijkllkjihgfedcbaa'))
