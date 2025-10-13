'''Given a string s, find the length of the longest substring without duplicate 
characters.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        chars = {}
        for right, ch in enumerate(s):
            if s[right] in chars and chars[ch] >= left:
                left = chars[ch] + 1
            chars[ch] = right
            max_length = max((right - left) + 1, max_length)
        return max_length
            
              
sol = Solution()
print(sol.lengthOfLongestSubstring(s = "abcabcbb")) #3
print(sol.lengthOfLongestSubstring(s = "bbbbb"))    #1
print(sol.lengthOfLongestSubstring(s = "pwswkew"))  #4