from time import time

# Write 3 functions on array nums
# f1(nums) -> 1+nums[0]
# f2(nums) -> sum(nums)
# f3(nums) -> pair(nums)

nums = [1, 2, 3]

def get_sum1(nums):
    start = time()
    result = 1+nums[0]
    end = time()
    print(f'Time taken for execution is:: {end-start}')
    return result

print(get_sum1(nums))

def get_sum2(nums):
    start = time()
    result = sum(nums)
    end = time()
    print(f'Time taken for execution is:: {end-start}')
    return result

print(get_sum2(nums))

def get_pairs(nums):
    start = time()
    result = []
    result = [(x, y) for x in nums for y in nums]
    end = time()
    print(f'Time taken for execution is:: {end-start}')
    return result

print(get_pairs(nums))
