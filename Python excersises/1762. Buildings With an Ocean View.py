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


# Most effective solution
def findBuildings2(heights):
    n = len(heights)
    answer = []

    for current in range(n):
        # If the current building is taller,
        # it will block the shorter building's ocean view to its left.
        # So we pop all the shorter buildings that have been added before.
        while answer and heights[answer[-1]] <= heights[current]:
            answer.pop()
        answer.append(current)

    return answer


heights = [1, 3, 2, 4]

print(findBuildings2(heights))
