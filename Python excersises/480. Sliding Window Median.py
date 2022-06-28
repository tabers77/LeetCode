import statistics as s

#  Create a generator where I grab only k characters [1  3  -1] -3  5  3  6  7
def sliding_window(l, split=2):
    for i in range(0, len(l)):
        yield l[i: i + split]


def medianSlidingWindow(nums, k: int) :
    lst = list(sliding_window(nums, k))
    filtered = [s.median(sorted(l)) for l in lst if len(l) == k]

    return filtered


nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(medianSlidingWindow(nums, k))

