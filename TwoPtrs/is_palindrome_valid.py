"""Leetcode problem 125: Valid Palindrome https://leetcode.com/problems/valid-palindrome/
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


"""
'What if you can delete at most one character and still want to check if it’s a palindrome?'
Leetcode Problem 680: Valid Palindrome II https://leetcode.com/problems/valid-palindrome-ii/
Space: O(n)
Time: O(1)
"""


def validPalindromeII(self, s: str) -> bool:
    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            skip_left = is_palindrome(left + 1, right)
            skip_right = is_palindrome(left, right - 1)
            return skip_left or skip_right
    return True


"""
'How would you check if a string streaming in real-time could form a palindrome?'
Append the characters as they come in and do the same algorithm
"""
