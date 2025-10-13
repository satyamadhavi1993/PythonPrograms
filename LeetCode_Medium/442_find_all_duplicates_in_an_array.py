'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output'''

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:     
        duplicates = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]
        return duplicates
             

sol = Solution()
print(sol.findDuplicates(nums = [4,3,2,7,8,2,3,1]))
print(sol.findDuplicates(nums = [1,1,2]))
print(sol.findDuplicates(nums = [1]))
