# Given an integer array nums, return true if any value appears at least twice in the 
# array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates = set()
        for num in nums:
            if num in duplicates:
                return True
            duplicates.add(num)
        return False
        


sol = Solution()
print(sol.containsDuplicate(nums = [1,2,3,4]))        
print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))      