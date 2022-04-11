from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    c1, c2 = Counter(ransomNote), Counter(magazine)

    # Counts the number of times a specific letter matched
    count = 0
    for letter in ransomNote:

        # Count only characters lower than letters in magazine
        if c1[letter] <= c2[letter]:
            count += 1

    length = len([i for i in ransomNote])
    if count == length:
        return True
    else:
        return False


ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))