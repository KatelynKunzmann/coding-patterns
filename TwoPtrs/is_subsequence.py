"""Leetcode Problem 392: Is Subsequence https://leetcode.com/problems/is-subsequence/
Time: O(n)
Space: O(1)
"""


def isSubsequence(self, s: str, t: str) -> bool:
    if s == t:
        return True
    sptr = 0
    tptr = 0
    while sptr < len(s) and tptr < len(t):
        if s[sptr] == t[tptr]:
            sptr += 1
        tptr += 1
    return sptr == len(s)
