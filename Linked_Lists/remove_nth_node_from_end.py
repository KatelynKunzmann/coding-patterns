from typing import Optional
from ds import ListNode

"""Leetcode Problem 19: Remove Nth Node From End Of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Time: O(n)
Space: O(1)
"""


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return None
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


"""What if the list has only 1 node and n = 1? (Should return None).
    
What if n equals the length of the list? (You remove the head).
    
What if n is bigger than the list length? (Your code currently returns the original head — worth pointing out).

What if head is None (empty list)?

Why not just start leader = trailer = head?

What happens if you try removing the head without a dummy?

Can you return an exception if n > length of the list?
Sure, raise ValueError("n is larger than the length of the list")
"""
