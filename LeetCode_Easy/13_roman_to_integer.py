class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000}
        result = 0

        for index in range(len(s)-1, -1, -1):
            char = s[index]
            if index == len(s) - 1:
                result = symbols[char]
            else:
                next_char = s[index + 1]
                if symbols[char] < symbols[next_char]:
                    result -= symbols[char]
                else:
                    result += symbols[char]
        return result

    
sol = Solution()
print(sol.romanToInt(s = "III"))
print(sol.romanToInt(s = "LVIII"))
print(sol.romanToInt(s = "MCMXCIV"))