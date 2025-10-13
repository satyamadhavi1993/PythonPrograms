'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.'''
from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
            if dict1[num] > len(nums)//2:
                return num
            
    
    def majorityElement2(self, nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
        
    
sol = Solution()
print(sol.majorityElement(nums = [3,2,3]))
print(sol.majorityElement(nums = [2,2,1,1,1,2,2]))
print(sol.majorityElement2(nums = [3,2,3]))
print(sol.majorityElement2(nums = [2,2,1,1,1,2,2]))
        