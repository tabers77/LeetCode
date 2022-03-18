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

# Solution 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret



l1 = ListNode(2)
l1.next(4)
l1.next(3)

l2 = ListNode(5)
l1.next(6)
l1.next(4)

s = Solution
print(s.addTwoNumbers(l1, l2))

