#  PEMDAS, which stands for: parentheses, exponents, multiplication and division from left to right,
#  and addition and subtraction from left to right.

# WORK IN PROGRESS
def calculate(s):

    chars = [i for i in s]
    signs = ['+', '-', '/', '*']
    res = []
    for idx, val in enumerate(chars):

        if chars[idx + 1] in signs and val not in signs:
            if chars[idx + 1] == '+':
                res.append(int(val) + int(chars[idx + 2]))
            elif chars[idx + 1] == '-':
                res.append(int(val) - int(chars[idx + 2]))
            elif chars[idx + 1] == '/':
                res.append(int(val) / int(chars[idx + 2]))
            elif chars[idx + 1] == '*':
                res.append(int(val) * int(chars[idx + 2]))

    return res


s = "3+2*2"
print(calculate(s))
