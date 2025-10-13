'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.'''

from collections import Counter

class Solution():
    def firstUniqChar(s):
        count = Counter(s)
        print(type(count))
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1


    def firstUniqChar2(s):
        count = [0] * 26
        for ch in s:
            x = ord(ch) - ord('a')
            count[x] += 1
        
        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            if count[index] == 1:
                return (ch, i)
        return -1

    def firstUniqChar3(s):
        count = [0] * 26
        for ch in s:
            x = ord(ch) - ord('a')
            count[x] += 1
        
        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            if count[index] == 1:
                return i
        return -1
    
 
sol = Solution()   
print(sol.firstUniqChar("leetcode"))  # 0
print(sol.firstUniqChar("aabb"))  
print(sol.firstUniqChar2("leetcode"))  # 0
print(sol.firstUniqChar2("aabb"))  
print(sol.firstUniqChar3("leetcode"))  # 0
print(sol.firstUniqChar3("aabb"))  