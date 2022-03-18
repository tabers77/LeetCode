from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    c1, c2 = Counter(ransomNote), Counter(magazine)
    count = 0
    for letter in ransomNote:
        if c1[letter] <= c2[letter]:
            count += 1

    l = len([i for i in ransomNote])
    if count == l:
        return True
    else:
        return False


ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))