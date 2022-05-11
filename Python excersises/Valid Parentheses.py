def isValid(s: str):
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    hash_map = {')': '(', ']': '[', '}': '{'}

    if len(s) <= 1 or s[0] in hash_map.keys():
        return False

    stack = []

    for bracket in s:
        # if open bracket append that bracket
        if bracket in hash_map.values():
            stack.append(bracket)
        # if stack is not empty and close bracket
        elif stack and bracket in hash_map.keys():
            # if that bracket is equals to the last open bracket remove last character
            if hash_map[bracket] == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)

    return len(stack) == 0


s = "(])"
print(isValid(s))
