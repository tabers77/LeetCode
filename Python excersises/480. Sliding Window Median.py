class Solution:

    def sliding_window(self, l, split=2):
        for i in range(0, len(l)):
            yield l[i: i + split]

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = list(self.sliding_window(nums, k))
        filtered = [s.median(sorted(l)) for l in lst if len(l) == k]

        return filtered