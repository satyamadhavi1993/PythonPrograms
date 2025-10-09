def two_sum(haystack, needle):
    n = len(needle)
    m = len(haystack)
    for s in range(0, m+1-n):
        for i in range(n):
            if not haystack[s + i] == needle[i]:
                break
            if i == n - 1:
                return s
    return -1

print(two_sum(haystack = "sadbutsad", needle = "but"))
print(two_sum(haystack = "leetcode", needle = "leeto"))