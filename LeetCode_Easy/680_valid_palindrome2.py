'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.'''
class Solution:
    def checkPalindrome(self, s: str, left: int, right: int):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try skipping one character (either left or right)
                return self.checkPalindrome(s, left + 1, right) or self.checkPalindrome(s, left, right - 1)
            left += 1
            right -= 1

        return True
    
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysdgvhsmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
sol = Solution()
print(sol.validPalindrome(s))