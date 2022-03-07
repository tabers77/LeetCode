# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Solution 1

def addTwoNumbers(l1,l2):

    def return_number_backward(l, lst_mode=False):

        m = len(l)
        n = ''
        for i in range(len(l)):
            idx = m - (i + 1)
            n += str(l[idx])
        reversed_list = [int(i) for i in n]

        return int(n) if not lst_mode else reversed_list

    n1 = return_number_backward(l1)
    n2 = return_number_backward(l2)

    r = str(n1 + n2)

    lst_r = [i for i in r]

    return return_number_backward(lst_r, lst_mode=True)

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(addTwoNumbers(l1, l2))

