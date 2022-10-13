def findBuildings(heights):
    match = []

    heights.append(0)

    for idx, b in enumerate(heights):
        if idx < len(heights) - 1:
            count = 0
            for j in heights[idx + 1:]:
                if j < heights[idx]:
                    count += 1
            if count == len(heights[idx + 1:]):
                match.append(idx)

    return match


heights = [1, 3, 2, 4]

print(findBuildings(heights))
