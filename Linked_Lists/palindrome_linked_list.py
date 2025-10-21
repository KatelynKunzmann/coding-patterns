from ds import ListNode

"""Leetcode Problem 234: Palindrome Linked List https://leetcode.com/problems/palindrome-linked-list/
Time: O(n)
Space: O(n)
"""


def palindromic_linked_list(head: ListNode) -> bool:
    if not head or not head.next:
        return True
    node_list = []
    curr_node = head
    while curr_node:
        node_list.append(curr_node.val)
        curr_node = curr_node.next

    left, right = 0, len(node_list) - 1
    while left < right:
        if node_list[left] != node_list[right]:
            return False
        left += 1
        right -= 1
    return True


"""
'Is there a more optimal space solution?'
Yes, there is an O(1) space solution:
1) Finding the middle: Slow moves 1 step, fast moves 2 steps → when fast reaches the end, slow is at the middle.
2) Reversing the second half: Classic in-place reversal.
3) Comparing halves: Compare nodes from the start and from the reversed second half. If all match → palindrome.
"""


def palindromic_linked_list_optimal(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Step 3: Compare the first half and the reversed second half
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True
