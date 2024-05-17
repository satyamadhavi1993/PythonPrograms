def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right :
        arr[right], arr[left] = arr[left], arr[right]
        left += 1
        right -= 1
    return arr


print(reverse_in_place(['python', 'java', 'c', 'c#', 'ruby']))
