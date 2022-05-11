def myAtoi(input):
    sign = 1
    result = 0
    index = 0
    n = len(input)

    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2, 31)

    # Discard all spaces from the beginning of the input string.
    while index < n and input[index] == ' ':
        index += 1

    # sign = +1, if it's positive number, otherwise sign = -1.
    if index < n and input[index] == '+':
        sign = 1
        index += 1
    elif index < n and input[index] == '-':
        sign = -1
        index += 1

    # Traverse next digits of input and stop if it is not a digit.
    # End of string is also non-digit character.
    while index < n and input[index].isdigit():
        digit = int(input[index])

        # Check overflow and underflow conditions.
        if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            # If integer overflowed return 2^31-1, otherwise if underflow return -2^31.
            return INT_MAX if sign == 1 else INT_MIN

        # Append current digit to the result.
        result = 10 * result + digit
        index += 1

    # We have formed a valid number without any overflow/underflow.
    # Return it after multiplying it with its sign.
    return sign * result


# Solution 2 - work in progress
# level1 is string is numeric

def myAtoi(s: str):

    sign = '+'
    result = ''
    sp = [i for i in s]

    i = 0

    while i < len(sp):
        for j in range(len(sp)-1):
            print(j)
            if sp[j] == '':
                pass
            if sp[j].isdigit() or sp[j] in ('+', '-'):

                if sp[j] in ('+', '-') or sp[j + 1] in ('+', '-'):
                    sign = sp[j]
                else:
                    result += sp[j]
            else:
                result += 0
            i += 1

    return result


s = "42"

print(myAtoi(s))