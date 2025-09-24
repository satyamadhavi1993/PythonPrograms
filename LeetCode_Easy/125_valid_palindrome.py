'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.'''
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = re.sub(r'[^a-z0-9]', "", s)
        if len(s2) == 0:
            return True
        left = 0
        right = len(s2) - 1
        while (left < right):
            if s2[left] != s2[right]:
                return False
            left += 1
            right -= 1
        return True
    
    
sol = Solution()
print(f"Is Palindrome: {sol.isPalindrome("A man, a plan, a canal: Panama")}")
print(f"Is Palindrome: {sol.isPalindrome("race a car")}")
print(f"Is Palindrome: {sol.isPalindrome(" ")}")
print(f"Is Palindrome: {sol.isPalindrome("0P")}")