
class SparseVector:
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        res = 0

        for i in range(len(self.array)):
            res += self.array[i] * vec.array[i]

        return res


nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)

print(v1.dotProduct(v2))
