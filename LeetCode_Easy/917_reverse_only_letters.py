'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            if not s[left].isalpha():
                left += 1
            if not s[right].isalpha():
                right -= 1
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
    
sol = Solution()
print(sol.reverseOnlyLetters(s = "ab-cd"))
print(sol.reverseOnlyLetters(s = "Test1ng-Leet=code-Q!"))