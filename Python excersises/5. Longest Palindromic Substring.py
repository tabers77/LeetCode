def longestPalindrome(s: str) -> str:
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2 , the -1 will go backwards
            if len(m) >= j - i:  # To reduce time
                break
            # s[i:j] the string will be reduced each time
            # s[i:j][::-1] take the same word in reverse
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    return m


s = "babad"

longestPalindrome(s)

