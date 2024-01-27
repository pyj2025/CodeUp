import heapq
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        curr = list3
        data = []

        while list1:
            heapq.heappush(data, list1.val)
            list1 = list1.next

        while list2:
            heapq.heappush(data, list2.val)
            list2 = list2.next

        while data:
            val = heapq.heappop(data)
            curr.next = ListNode(val)
            curr = curr.next

        return list3.next
