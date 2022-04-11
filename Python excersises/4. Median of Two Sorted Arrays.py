import statistics


def findMedianSortedArrays(nums1, nums2):

    nums3 = nums1 + nums2
    print(nums3)
    return statistics.median(nums3)


nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1,nums2))

