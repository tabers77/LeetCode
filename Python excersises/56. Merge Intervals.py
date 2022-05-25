def n_overlaps(a, b):
    first_interval_range = [n for n in range(a[0], a[-1] + 1)]
    second_interval_range = [n for n in range(b[0], b[-1] + 1)]
    count = 0
    for i in second_interval_range:
        if i in first_interval_range:
            count += 1
    if count != 0:
        return True
    else:
        return False


def merge(intervals):
    # 1. Create a sorted list
    intervals = sorted(intervals)

    # 2. Return interval if there is only 1 interval
    if len(intervals) == 1:
        return intervals

    i = 0
    while i < len(intervals) - 1:
        # If there is an overlap between first and second character find the min and max
        # Replace value with the new interval and remove the second character
        if n_overlaps(intervals[i], intervals[i + 1]):
            mixed = intervals[i] + intervals[i + 1]
            min_ = min(mixed)
            max_ = max(mixed)
            new_interval = [min_, max_]
            intervals[i] = new_interval
            intervals.pop(i + 1)

        # If there is no overlap between first and second character keep the first character and continue to next char
        else:
            i += 1

    return intervals


# Solution 2 - Best solution

def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, simply append it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)

        else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]

print(merge(intervals))
