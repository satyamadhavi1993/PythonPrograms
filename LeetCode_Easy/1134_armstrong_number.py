'''
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.
'''

class Solution:
    def isArmstrong(self, n: int) -> bool:
        num_of_digits = len(str(n))
        temp = n
        result = 0
        while temp > 0:
            result += (temp % 10) ** num_of_digits
            temp //= 10
        return result == n
    
sol = Solution()
print(sol.isArmstrong(n = 123))
print(sol.isArmstrong(n = 2))
print(sol.isArmstrong(n = 153))