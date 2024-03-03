"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        curr = head

        if curr.next is None:
            return head

        prev = None

        while curr.next is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        head = curr

        return head
