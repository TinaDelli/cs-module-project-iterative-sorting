def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    high = len(arr) - 1 
    low = 0
    while True:
        middle = (low + high)//2
        if low > high or len(arr) == 0:
            return -1
        elif arr[middle] == target:
            return middle
        elif target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else: 
            return middle
    return -1  # not found
