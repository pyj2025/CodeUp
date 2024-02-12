# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        p1 = head
        p2 = prev
        while p1 and p2:
            next_p1 = p1.next
            next_p2 = p2.next
            p1.next = p2
            p2.next = next_p1
            p1 = next_p1
            p2 = next_p2