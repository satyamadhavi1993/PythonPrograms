'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1        
    
    
sol = Solution()
print(sol.isPowerOfThree(n = 27))
print(sol.isPowerOfThree(n = 0))
print(sol.isPowerOfThree(n = -1))