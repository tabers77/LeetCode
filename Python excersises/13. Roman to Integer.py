# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


def romanToInt(s: str):

    # dict with values
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    counter = 0
    i = 0
    while i < len(s):
        # if number is lower than next number take next number and subtract by number
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            counter += roman_map[s[i+1]] - roman_map[s[i]]
            # here I count 2 and move 2 steps since I am reading more than 1 number or 2
            i += 2
        else:
            # if number is not lower than next number use the value of the current number
            counter += roman_map[s[i]]
            # here I count 1 since I am reading only 1 number
            i += 1
    return counter


s = "VI"

print(romanToInt(s))


