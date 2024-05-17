def using_recursion(i):
    if i == 1:
        return 1
    
    return i * using_recursion(i - 1)


print(using_recursion(5))
