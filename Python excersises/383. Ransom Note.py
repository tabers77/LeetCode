from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        count = 0
        for i in ransomNote:
            if c1[i] <= c2[i]:
                count += 1
        l = len([i for i in ransomNote])
        if count == l:
            return True
        else:
            return False
