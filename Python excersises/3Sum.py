from itertools import permutations

# Incorrect solution

class Solution(object):
    def zero_sum_check(self, tup):
        if sum(tup) == 0:
            return True
        else:
            return False

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # such that i != j, i != k
        # and j != k, and nums[i] + nums[j] + nums[k] == 0
        triplets = list(permutations(nums, 3))
        stack = list()
        for comb in triplets:
            if self.zero_sum_check(comb):
                stack.append(comb)
        # Sort tuples
        stack = set(stack)
        sorted_stack = sorted([sorted(tup) for tup in stack])

        final_stack = []
        if len(sorted_stack) > 1:
            for i in range(len(sorted_stack) - 1):
                if sorted_stack[i] == sorted_stack[i + 1] and sorted_stack[i] not in final_stack:
                    final_stack.append(sorted_stack[i])
        else:
            return sorted_stack

        return final_stack


# Main solution

def threeSum(nums):
    res, dups = set(), set()
    seen = {}
    for i, val1 in enumerate(nums):
        if val1 not in dups:
            # if value not in set add it
            dups.add(val1)
            # enumerate from one step to the right
            for j, val2 in enumerate(nums[i + 1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
    return res

nums = [-4,-1,-1, 0,1,2]

print(threeSum(nums))



