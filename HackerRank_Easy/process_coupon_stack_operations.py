import math
import os
import random
import re
import sys

def processCouponStackOperations(operations):
    stack = []
    result = []
    for op in operations:
        parts = op.split()
        if parts[0] == "push":
            stack.append(int(parts[1]))
        elif parts[0] == "pop":
            if stack:
                stack.pop()
        elif parts[0] == "top":
            result.append(stack[-1] if stack else "Empty")
        elif parts[0] == "getMin":
            result.append(min(stack) if stack else "Empty")
    return result
   
   
if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
