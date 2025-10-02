from typing import List
from collections import defaultdict

""" Leetcode problem 49: Group Anagrams https://leetcode.com/problems/group-anagrams/
1) Use defaultdict because we don't want keyerrors; groups starts empty and any new key automatically gets an empty list. 
2) Iterate through strs - creating keys based on their sorted string
3) Assign values to the keys that are the original string
4) return the values as a list explained below
After processing all strings, groups looks like this:
{
    "abt": ["bat"],
    "ant": ["nat", "tan"],
    "aet": ["ate", "eat", "tea"]
}
groups.values() returns a view of all the dictionary’s values:
    dict_values([["bat"], ["nat","tan"], ["ate","eat","tea"]])

Wrapping it in list() converts that view into an actual list:
    list(groups.values())
    # [["bat"], ["nat","tan"], ["ate","eat","tea"]]

Time: O(n⋅klogk)
n = number of strings in strs
k = maximum length of a string
for s in strs: → iterates n strings → O(n) iterations
sorted(s) → sorts a string of length k → O(k log k)
"".join(sorted(s)) → joins k characters → O(k)
So each string costs O(k log k + k) = O(k log k)
Appending to dictionary → O(1) amortized

Space: O(nk)
Dictionary groups: stores all strings grouped → O(nk) (all characters)
Key key = "".join(sorted(s)) → temporary string of length k → O(k)
Sorted list from sorted(s) → O(k) temporarily
So extra space outside the output → O(k) per iteration
Total space including output → O(nk)
"""


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


"""
There is a more optimal solution (for time) but a little too complicated - Fixed size array solution
    Time: O(nk) — linear in total characters, faster than sorting approach
"""
