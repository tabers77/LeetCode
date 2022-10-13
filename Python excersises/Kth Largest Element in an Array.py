# -----------
# SOLUTION 1
# -----------
def findKthLargest(nums, k):
    sorted_list = sorted(nums)
    return sorted_list[-k]


nums = [3, 2, 1, 5, 6, 4]
k = 2

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(findKthLargest(nums, k))

# -----------
# SOLUTION 2
# -----------
