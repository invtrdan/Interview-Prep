# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num, n1 = 0, 1
        curr1 = l1
        while curr1.next:
            num += curr1.val * n1
            curr1 = curr1.next
            n1 *= 10
        num += curr1.val * n1

        n2 = 1
        curr2 = l2
        while curr2.next:
            num += curr2.val * n2
            curr2 = curr2.next
            n2 *= 10
        num += curr2.val * n2

        number = str(num)

        l3 = ListNode(number[-1])
        curr = l3
        i = len(number) - 2
        while i > -1:
            curr.next = ListNode(number[i])
            curr = curr.next
            i -= 1

        return l3
