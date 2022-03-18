def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    ans = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            # if letter in map take the max between the count of that letter and i
            i = max(mp[s[j]], i)

        # This will return the length of a substring
        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1
    return ans


s = "pwwkew"
print(lengthOfLongestSubstring(s))
