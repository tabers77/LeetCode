
def maxArea(height):
    res = 0
    # Here I take len(height) - 1
    # left from the start and right from the end
    l, r = 0, len(height) - 1
    while l < r:
        # Area: with * height
        # Width = r - l
        # Compute the area (b * h)
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        # if height left is lower then I move 1 space to the right
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))