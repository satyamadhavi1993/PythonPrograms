'''Given an integer array nums, find the subarray with the largest sum, and return its sum.'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_subarr_sum = nums[0]
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_subarr_sum = max(max_subarr_sum, current_sum)
        return max_subarr_sum
    
    
sol = Solution()
print(sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))   # → 6  (subarray [4,-1,2,1])
print(sol.maxSubArray(nums = [1]))                       # → 1  (single element)
print(sol.maxSubArray(nums = [5,4,-1,7,8]))              # → 23 (whole array)
print(sol.maxSubArray(nums = [1,2,3]))                   # → 6  (whole array positive)
print(sol.maxSubArray(nums = [-1,-2,-3]))                # → -1 (largest single element)
print(sol.maxSubArray(nums = [0]))                       # → 0  (neutral value)
print(sol.maxSubArray(nums = [2,-1,2]))                  # → 3  (subarray [2,-1,2])
print(sol.maxSubArray(nums = [100000]))                  # → 100000  (single large positive)
print(sol.maxSubArray(nums = [-100000]))
print(sol.maxSubArray(nums = [1,-1,1,-1,1,-1,1]))        # → 1  (any single 1)
print(sol.maxSubArray(nums = [-2,1,-3,2,-1,2,-1]))       # → 3  (subarray [2,-1,2])
print(sol.maxSubArray(nums = [4,-1,2,1,-5,4]))           # → 6  (subarray [4,-1,2,1])
print(sol.maxSubArray(nums = [-8, -3, -6, -2, -5, -4]))  # → -2 (least negative single element)
print(sol.maxSubArray(nums = [3, -2, 5, -1]))            # → 6  (subarray [3,-2,5])
print(sol.maxSubArray(nums = [-2, -1, 0, 1, 2]))         # → 3  (subarray [0,1,2])
print(sol.maxSubArray(nums = [8, -19, 5, -4, 20]))       # → 21 (subarray [5,-4,20])
print(sol.maxSubArray(nums = [2, -8, 3, -2, 4, -10]))    # → 5  (subarray [3,-2,4])
print(sol.maxSubArray(nums = [1,1,1,1,1]))               # → 5  (whole array)
print(sol.maxSubArray(nums = [-1,0,-2,0,-3]))            # → 0  (single zero is max)
print(sol.maxSubArray(nums = [0, -3, 1, 1]))             # → 2  (subarray [1,1])
print(sol.maxSubArray(nums = [-2, 0, -1]))               # → 0  (zero alone)
print(sol.maxSubArray(nums = [100, -90, 80, -70, 60, -50, 40]))  # → 100 (first element best)
print(sol.maxSubArray(nums = [-10, 20, -5, 15, -10, 30, -25]))   # → 50  (subarray [20,-5,15,-10,30])
