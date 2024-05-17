# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def using_recursion(limit):
    if limit <= 1:
        return limit
    else:
        return (using_recursion(limit - 1) + using_recursion(limit - 2))

print(using_recursion(6))
