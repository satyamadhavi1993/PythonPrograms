"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        result[0] = 1
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        postfix = nums[-1]
        for i in range(n-2, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
        return result

    
sol = Solution()
print(sol.productExceptSelf(nums = [1,2,3,4]))
print(sol.productExceptSelf(nums = [5, 10, 2, 3]))
print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))
print(sol.productExceptSelf(nums = [0, 1, 2, 3]))        # → [6, 0, 0, 0]
print(sol.productExceptSelf(nums = [1, 2, 3, 0]))        # → [0, 0, 0, 6]
print(sol.productExceptSelf(nums = [0, 0, 2, 3]))        # → [0, 0, 0, 0]
print(sol.productExceptSelf(nums = [-1, 2, 3, 4]))       # → [24, -12, -8, -6]
print(sol.productExceptSelf(nums = [-1, -2, -3, -4]))    # → [-24, -12, -8, -6]
print(sol.productExceptSelf(nums = [-1, -2, -3]))        # → [6, 3, 2]
print(sol.productExceptSelf(nums = [0, -1, 2, -3]))      # → [6, 0, 0, 0]
print(sol.productExceptSelf(nums = [7]))                 # → [1]  (edge case: typically defined as 1)
print(sol.productExceptSelf(nums = [1, 0]))              # → [0, 1]
print(sol.productExceptSelf(nums = [1, 2]))              # → [2, 1]
print(sol.productExceptSelf(nums = [1, 1, 1, 1]))        # → [1, 1, 1, 1]
print(sol.productExceptSelf(nums = [2, 2, 2, 2]))        # → [8, 8, 8, 8]