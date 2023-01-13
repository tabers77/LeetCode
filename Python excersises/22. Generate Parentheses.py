def generateParenthesis(n: int):
    stack = []
    res = []

    def backTrack(openN, closedN):
        if openN == closedN == n:
            res.append(''.join(stack))
            return
        if openN < n:
            stack.append('(')
            backTrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(')')
            backTrack(openN, closedN + 1)
            stack.pop()

    backTrack(0, 0)

    return res


n = 3
print(generateParenthesis(n))
