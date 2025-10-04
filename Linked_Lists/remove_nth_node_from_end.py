from typing import Optional
from ds import ListNode

"""Leetcode Problem 19: Remove Nth Node From End Of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Time: O(n)
Space: O(1)
"""


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(-1)
    dummy.next = head
    leader = trailer = dummy
    for _ in range(n):
        leader = leader.next
        if not leader:
            return head
    while leader.next:
        leader = leader.next
        trailer = trailer.next
    trailer.next = trailer.next.next
    return dummy.next
