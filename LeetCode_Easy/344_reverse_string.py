# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while(left < right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            left += 1
            right -= 1
        return s
                  

sol = Solution()
s = ["h","e","l","l","o"]
print(f"{s} - {sol.reverseString(s)}")