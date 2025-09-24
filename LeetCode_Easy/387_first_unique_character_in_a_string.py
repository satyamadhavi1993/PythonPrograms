from collections import Counter

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
    
    
print(firstUniqChar2("leetcode"))  # 0
print(firstUniqChar2("aabb"))  