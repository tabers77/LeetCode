def isMatch(s: str, p: str) -> bool:

    def dfs(i, j):

        if i >= len(s) and j >= len(p):
            return True

        if j >= len(p):
            return False

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        if (j + 1) < len(p) and p[j + 1] == '*':
            return dfs(i, j + 2) or match and dfs(i + 1, j)
        if match:
            return dfs(i + 1, j + 1)
        return False

    return dfs(0, 0)


def isMatch(text, pattern):

    # if there is no pattern check if the text exists
    if not pattern:
        return not text

    # Match: if there is text and first pattern character is equal first character of s or .
    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        # check if it is a match from second character of pattern or ...
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


s = "aa"
p = "a*"

print(isMatch(s, p))

