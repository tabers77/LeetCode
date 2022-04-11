# Brute force

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

# Two-pass Hash Table
def twoSum(nums, target):

    # Enumerate elements
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    print(f'Hash map: {hashmap}')

    for i in range(len(nums)):
        complement = target - nums[i]# 7
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]

nums = [2,7,11,15]

target = 9

print(twoSum(nums, target))