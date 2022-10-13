
def convert(s: str, numRows: int):
    if numRows == 1:
        return s
    res = ""
    for r in range(numRows):
        # Here we compute how much we will be incrementing each time
        increment = 2 * (numRows - 1)
        for i in range(r, len(s), increment):
            res += s[i]
            # Check that we are in the middle row
            if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                res += s[i + increment - 2 * r]
    return res


s = "PAYPALISHIRING"

print(convert(s=s, numRows=3))
