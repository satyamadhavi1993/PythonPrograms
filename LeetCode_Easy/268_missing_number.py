'''Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1))//2
        for n in nums:
            total -= n
        return total
    
    def missingNumber2(nums):
        n = len(nums)
        total = 0
        for i in range(n + 1):
            total += i
        for num in nums:
            total -= num
        return total
    
    
sol = Solution()
print(sol.missingNumber([3,0,1]))  # 2
print(sol.missingNumber([0,1]))    # 2
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))  # 8

print(sol.missingNumber2([3,0,1]))  # 2
print(sol.missingNumber2([0,1]))    # 2
print(sol.missingNumber2([9,6,4,2,3,5,7,0,1]))  # 8