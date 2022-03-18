import math

# Solution 1
def reverse(x: int) :
    MIN = - 2147483648
    MAX = 2147483648
    ans = 0
    while x:
        digit = int(math.fmod(x, 10))
        x = int(x / 10)
        if ans > MAX // 10 or (ans == MAX // 10 and digit >= MAX % 10):
            return 0
        if ans < MIN // 10 or (ans == MIN // 10 and digit <= MIN % 10):
            return 0
        ans = (ans * 10) + digit

    return ans


# Solution 2

def reverse (x: int):
    # If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    def check_32_bit(x):
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return True

    if check_32_bit(x):
        return 0
    else:
        strg = str(x)
        if x >= 0:
            # reverse the string
            revst = strg[::-1]
        else:
            # Take the symbol from char 1 and reverse it
            temp = strg[1:]
            temp2 = temp[::-1]
            revst = "-" + temp2

        if check_32_bit(int(revst)):
            return 0
        else:
            return int(revst)


x = -123
print(reverse(x))