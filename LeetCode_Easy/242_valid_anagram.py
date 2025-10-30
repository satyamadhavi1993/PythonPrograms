'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        return all(c == 0 for c in count)
    
    def isAnagram2(self, s, t):
        if not len(s) == len(t):
            return 0
        letters = [0] * 26
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] += 1
        
        return all(letters)
            
    
    
sol = Solution()
print(f"Is Anagram: {sol.isAnagram("anagram", "nagaram")}")
print(f"Is Anagram: {sol.isAnagram("rat", "car")}")
print(f"Is Anagram: {sol.isAnagram2("anagram", "nagaram")}")
print(f"Is Anagram: {sol.isAnagram2("rat", "car")}")