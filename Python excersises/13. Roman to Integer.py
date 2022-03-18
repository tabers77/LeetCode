# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

def romanToInt(s: str):

    # dict with values
    roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}

    counter = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            counter += roman_map[s[i+1]] - roman_map[s[i]]
            i += 2
        else:
            counter += roman_map[s[i]]
            i += 1
    return counter

s = "MCMXCIV"

print(romanToInt(s))


