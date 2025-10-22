"""Leetcode Problem 9: Palindrome Number https://leetcode.com/problems/palindrome-number/
Reverse number by peeling off each digit from original number (modulo by 10)
Construct new number: New number is constructed by multiplying itself by 10 -> Creating the next 10s place for that remainder
Add the remainder to the new number
Divide original number by 10
Time: O(log base 10 (n)) - one loop per digit
Space: O(1)
"""


def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num


"""
More optimal solution requires only having to do half of the number
"""
