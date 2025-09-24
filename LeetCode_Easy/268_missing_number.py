# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.


def missingNumber(nums):
    n = len(nums)
    total = 0
    for i in range(n + 1):
        total += i
        
    for num in nums:
        total -= num
    
    return total
    
    
# Test
print(missingNumber([3,0,1]))  # 2
print(missingNumber([0,1]))    # 2
print(missingNumber([9,6,4,2,3,5,7,0,1]))  # 8