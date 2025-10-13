from collections import defaultdict

class Solution:
    def char_frequency(self, s: str):
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        return dict(freq)
        
    
sol = Solution()
print(sol.char_frequency(s = "leetcode"))