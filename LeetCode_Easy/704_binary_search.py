def binarySearch(nums, target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1
    
    
# Test
print(binarySearch([-1,0,3,5,9,12], 9))  # 4