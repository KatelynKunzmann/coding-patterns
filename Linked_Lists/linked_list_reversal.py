from ds import ListNode

"""Leetcode Problem 206: Reverse Linked List https://leetcode.com/problems/reverse-linked-list/
1) Initialize node pointers (curr and prev)
2) Save a reference to the next node
3) Change the current node's next pointer to the previous node
4) Move both previous node and current node accordingly
5) Return the head
Time: O(n)
Space: O(1)
"""
"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


def linked_list_reversal(head: ListNode) -> ListNode:
    if not head:
        return None
    curr_node = head
    prev_node = None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node


"""
'Can you solve this using recursion'
Yes, by reversing the list starting from head.next and returning new head
Time: O(n)
Space: O(n) for the stack build up to n levels for n calls
"""


def linked_list_reversal_recursive(head: ListNode) -> ListNode:
    # Base Case
    if (not head) or (not head.next):
        return head
    # Recursively reverse the sublist starting from the next node
    new_head = linked_list_reversal_recursive(head.next)
    # After stack builds up, flip their links and return new head
    head.next.next = head
    head.next = None
    return new_head


"""
Example: 1 → 2 → 3 → None
    Call with head=1 → goes deeper
    Call with head=2 → goes deeper
    Call with head=3 → base case, return 3
    
    linked_list_reversal_recursive(1)
        linked_list_reversal_recursive(2)
            linked_list_reversal_recursive(3)
                return 3
            process node 2
        process node 1
    return 3


    On the way back up (unwinding the stack):
    head=2: head.next = 3
      → set 3.next = 2 (so 3 → 2)
      → set 2.next = None (cut old link)
      returns 3

    head=1: head.next = 2
      → set 2.next = 1 (so 2 → 1)
      → set 1.next = None
      returns 3
"""
