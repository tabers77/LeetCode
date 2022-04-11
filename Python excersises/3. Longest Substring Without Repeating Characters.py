# Brute force
def lengthOfLongestSubstring(s: str):
    def check(start, end):
        chars = [0] * 128
        for i in range(start, end + 1):
            c = s[i]
            chars[ord(c)] += 1
            if chars[ord(c)] > 1:
                return False
        return True

    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res



# Sliding window
def lengthOfLongestSubstring(s: str) -> int:
    ans = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(len(s)):
        if s[j] in mp:
            # if letter in map take the max between the count of that letter and i
            i = max(mp[s[j]], i)

        # This will return the length of a substring
        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1
    return ans

s = "pwwkew"
print(lengthOfLongestSubstring(s))
