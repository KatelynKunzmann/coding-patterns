""" Leetcode problem 125: Valid Palindrome https://leetcode.com/problems/valid-palindrome/
    Two pointers, inward traversal at same time
    if != to each other then return false
    ensure to skip non-alphanumeric chars and spaces
        If ptr hits non-alphanumeric char, progress only that one
    When ptrs meet, return true
    edge cases:
        2 non-alpha chars in a row
        empty string
Time: O(n)
Space: O(1)
"""

def is_palindrome_valid(s: str) -> bool:    
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True