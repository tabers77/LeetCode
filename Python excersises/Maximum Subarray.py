def maxSubArray(nums):
    maxSub = nums[0]
    current_sum = 0
    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num

        # Here I store the maximum sum all the time
        maxSub = max(maxSub, current_sum)
    return maxSub

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubArray(nums))
