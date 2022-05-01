def isValid(s: str):
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    hash_map = {')': '(', ']': '[', '}': '{'}

    stack = []
    if len(s) <= 1 or s[0] in hash_map.keys():
        return False

    for bracket in s:
        
        if bracket in hash_map.values():
            stack.append(bracket)

        elif stack and bracket in hash_map.keys():
            if hash_map[bracket] == stack[-1]:

                stack.pop()
            else:
                stack.append(bracket)
        print(bracket, stack)

    return len(stack) == 0


s = "{[]}"
s = "()"
s = "(]"
s = "()[]{"
s= "]"
s = "){"
s= "(){}}{"
s= "(])"
print(isValid(s))
