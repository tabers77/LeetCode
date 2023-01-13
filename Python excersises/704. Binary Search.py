def search(nums, target: int):
    c = {v: idx for idx, v in enumerate(nums)}
    if target in c.keys():
        return c[target]
    else:
        return -1
    # nums = sorted(nums)

# BINARY SEARCH

def binary_search(nums, target):
    # Set the left and right boundaries
    left = 0
    right = len(nums) - 1

    # Under this condition
    while left <= right:
        # Get the middle index and the middle value.
        mid = (left + right) // 2

        # Case 1, return the middle index.
        if nums[mid] == target:
            return mid
        # Case 2, discard the smaller half.
        elif nums[mid] < target:
            left = mid + 1
            # Case 3, discard the larger half.
        else:
            right = mid - 1

    # If we finish the search without finding target, return -1.
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

nums = [-1, 0, 3, 5, 9, 12]

target = 2
print(binary_search(nums, target))
