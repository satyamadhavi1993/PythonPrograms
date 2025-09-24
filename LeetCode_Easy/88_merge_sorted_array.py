class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        
        for i in range(m+n-1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
        return nums1
    
    
    
sol = Solution()
print(sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))