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


""" More optimal solution than both of these - fixed size array solution with ord()
        Time: O(n)
        Space: O(1) (array size 26, constant)
"""

def isAnagramOptimal(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = [0] * 26  # one slot for each letter a-z

    for c in s:
        counts[ord(c) - ord('a')] += 1

    for c in t:
        counts[ord(c) - ord('a')] -= 1

    # if all counts are zero, it’s an anagram
    return all(x == 0 for x in counts)

"""
'What if the input strings include all unicode characters and we want to treat accented letters the same as unaccented letters?'
We could import the unicodedata libary and normalize the characters.
Then use the Counter solution on the normalized strings. See Below (also accounts for case insensitivity and whitespace)
Time: Still O(n)
Space: O(n) now because ~150,000 unicode characters
"""


from collections import Counter
import unicodedata

def isAnagram(s: str, t: str) -> bool:
    def normalize(text: str) -> str:
        # 1. Normalize Unicode (e.g., é → e + ´)
        text = unicodedata.normalize('NFKD', text)
        # 2. Keep only alphanumeric characters
        text = ''.join(c for c in text if c.isalnum())
        # 3. Lowercase everything
        return text.lower()
    
    return Counter(normalize(s)) == Counter(normalize(t))

