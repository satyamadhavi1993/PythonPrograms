# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



def two_sum(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        num = target - nums[i]
        if num in dict1:
            return (dict1[num], i)
        dict1[nums[i]] = i



nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))