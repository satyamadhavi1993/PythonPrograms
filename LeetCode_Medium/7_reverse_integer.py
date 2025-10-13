'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).'''

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = 2**31 - 1
        MAX_INT = 2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x > 0:
            last_digit = x % 10
            x //= 10
            if rev > (MAX_INT - last_digit) // 10:
                return 0
            rev = rev * 10 + last_digit
        return rev * sign
      
    
sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))