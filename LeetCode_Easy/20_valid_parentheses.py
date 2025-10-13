class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c not in mapping.keys() and c not in mapping.values():
                continue
            if c in mapping.values():
                stack.append(c)
            else:
                if not stack or not stack[-1] == mapping[c]:
                    return False
                stack.pop()
        return not stack            
    
    
sol = Solution()
print(sol.isValid("if (a[0] > b[1]) { doSomething(); }"))
print(sol.isValid("{[()]()}"))
print(sol.isValid("([)]"))
print(sol.isValid(""))
