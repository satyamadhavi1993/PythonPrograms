'''
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            anagrams_dict[key].append(str)
        return list(anagrams_dict.values())
    
sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams(strs = [""]))
print(sol.groupAnagrams(strs = ["a"]))
