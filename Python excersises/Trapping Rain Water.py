def trap(height):

    """Main formula: min(l,r) - height[i]"""

    # 1 Compute max left and max right
    left_init_stack = []
    max_left = []
    max_right = []

    for i in range(len(height)):
        if i == 0:
            # Start with a 0
            max_left.append(0)
        else:
            left_init_stack.append(height[i - 1])
            max_left.append(max(left_init_stack))

            max_right.append(max(height[i:]))

    max_right.append(0)

    # 2 Compute max left and max right - Apply main formula
    counter = 0
    for i in range(len(height)):
        minimum = min(max_left[i], max_right[i])
        main_computation = minimum - height[i]

        counter += 0 if main_computation <= 0 else main_computation

    return counter


height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))