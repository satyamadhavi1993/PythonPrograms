class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if not m:
            return -1
        for i in range((n+1) - m):
            for j in range(m):
                if not haystack[i+j] == needle[j]:
                    break
                if j == m-1:
                    return i
        return -1
                    

sol = Solution()
print(sol.strStr(haystack = "sadbutsad", needle = "but"))