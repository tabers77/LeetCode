# Solution 1
from typing import Optional


def addTwoNumbers(l1, l2):
    def return_number_backward(l, reversed=False):
        m = len(l)
        n = ''
        for i in range(len(l)):
            idx = m - (i + 1)
            n += str(l[idx])
        reversed_list = [int(i) for i in n]

        return int(n) if not reversed else reversed_list

    n1 = return_number_backward(l1)
    n2 = return_number_backward(l2)

    r = str(n1 + n2)

    lst_r = [i for i in r]

    return return_number_backward(lst_r, reversed=True)


# Solution 1 (proper solution)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next


l1 = ListNode(2)
l1.next(4)
l1.next(3)

l2 = ListNode(5)
l1.next(6)
l1.next(4)

s = Solution
print(s.addTwoNumbers(l1, l2))
