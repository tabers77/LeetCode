# Solution 2
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = []
    print(list(zip(*strs)))

    for x in zip(*strs):
        if len(set(x)) == 1:
            prefix.append(x[0])
        else:
            break

    return "".join(prefix)

# Solution 1

def longestCommonPrefix(strs):

    if len(strs) == 0 :
        return ''
    if len(strs) == 1:
        return strs[0]

    # Choose the prefix as an starting point
    prefix = strs[0]
    plen =len(prefix)

    for s in strs[1:]:
        while prefix != s[0:plen]:
            print(s[0:plen])
            prefix = prefix[0:plen-1]
            print(prefix)
            plen -= 1

            if plen == 0:
                return ''

    return prefix

strs = ["flower", "flow", "flight"]

print(longestCommonPrefix(strs))

