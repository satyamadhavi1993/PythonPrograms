def findDuplicates(nums: list):
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] = -nums[index]
    return duplicates
         
        


# Example
print(findDuplicates([4,3,2,7,8,2,3,1]))  # [2,3]
print(findDuplicates([1,1,2]))            # [1]
print(findDuplicates([1]))                # []