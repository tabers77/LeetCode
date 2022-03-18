from collections import Counter

def deleteAndEarn(nums) -> int:
    points = Counter()
    max_number = 0
    # 1 Pre compute how many points we gain from taking an element
    for num in nums:
        points[num] += num

        max_number = max(max_number, num)

    print(points)
    print(max_number)

    def max_points(num):
        # Check for base cases
        if num == 0:
            return 0
        if num == 1:
            return points[1]

        # Apply recurrence relation (this is the key part)
        operation = max_points(num - 1), max_points(num - 2) + points[num]
        return max(operation)

    return max_points(max_number)

inputs = [2,2,3,3,3,4]

print(deleteAndEarn(inputs))