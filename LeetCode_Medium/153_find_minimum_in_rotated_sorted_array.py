from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
                
    
    
sol = Solution()
print(sol.findMin(nums=[17, 19, 2, 5, 7, 8, 9, 12, 14, 16]))
# Rotated by 2 times
print(sol.findMin(nums=[9, 12, 14, 16, 17, 19, 2, 5, 7, 8]))
# # Rotated by 6 times
print(sol.findMin(nums=[2, 5, 7, 8, 9, 12, 14, 16, 17, 19]))
# Rotated by 10 times