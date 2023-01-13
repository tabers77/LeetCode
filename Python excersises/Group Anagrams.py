def groupAnagrams(strs):
    d = [(word, ''.join(sorted(word))) for word in strs]
    cont = dict()
    for tup in d:
        cont.setdefault(tup[1], []).append(tup[0])

    return list(cont.values())


inp =["",""] #["eat", "tea", "tan", "ate", "nat", "bat"] #["",""] #["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(groupAnagrams(inp))
