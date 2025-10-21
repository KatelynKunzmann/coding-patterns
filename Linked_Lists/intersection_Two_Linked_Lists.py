from ds import ListNode
from typing import Optional

"""Leetcode Problem 160: Intersection of Two Linked Lists https://leetcode.com/problems/intersection-of-two-linked-lists/
Each pointer keeps switching lists until they eventually meet at the intersection, therefore each pointer will travel
the total length of both lists combined:
Ex: len(A) + len(B) = 6 + 4 = 10 steps

Each pointer touches every node in List A once, and every node in List B once — never more than that.
List A:  1 → 3 → 5 → 7 → 9 → 11
                     ↑
List B:       2 → 4 —

Time: O(m + n) — each pointer traverses both lists exactly once.
Space: O(1)
"""


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    ptrA = headA
    ptrB = headB

    while ptrA != ptrB:
        # Move ptrA forward, or switch to headB when it is none (reaches the end)
        ptrA = ptrA.next if ptrA else headB

        # Move pointerB forward, or switch to headA when it is none (reaches the end)
        ptrB = ptrB.next if ptrB else headA

    return ptrA
