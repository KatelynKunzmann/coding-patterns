from collections import Counter

"""Leetcode problem 242: Valid Anagram https://leetcode.com/problems/valid-anagram/
1) If they aren't the same length, return False
2) Check if they are the same when sorted
Time: O(nlogn)
Space: O(n)
    - for storing the sorted strings
"""


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


"""
'What if the inputs contain Unicode characters? How would you adapt your solution to such a case?'
Python strings are Unicode by default and the equality check would still work

'Is there a more optimal solution?'
Yes, we could use Counter
Time: 
O(n) linear, since we iterate through strings once

Space: 
O(1) effectively, since only 26 lowercase letters

Counter is basically a frequency dictionary, example:
s = "anagram"
c = Counter(s)
print(c)
Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
"""


def isAnagramOptimized(s, t):
    return Counter(s) == Counter(t)


""" There is a more optimal solution than both of these, but it's a bit too complicated - fixed size array solution with ord()
        Time: O(n)
        Space: O(1) (array size 26, constant)
"""
