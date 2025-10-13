'''Given an integer array nums, return the third distinct maximum number 
in this array. If the third maximum does not exist, return the maximum number.'''


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first_max = second_max = third_max = float('-inf')
    
        for num in nums:
            if num == first_max or num == second_max or num == third_max:
                continue
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num
            
        if third_max == float('-inf'):
            return first_max
                
        return third_max
        
        
sol = Solution()
print(sol.thirdMax(nums = [3,2,1]))
print(sol.thirdMax(nums = [1,2]))
print(sol.thirdMax(nums = [2,2,3,1]))