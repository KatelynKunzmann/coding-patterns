from typing import List

""" Leetcode Problem 1: Two Sum https://leetcode.com/problems/two-sum/
In interviews, start by talking about brute force solving then transition to explaining this one, the more optimal one
Time: O(n)
Space: O(n)
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in num_map:
            return [num_map[comp], i]
        num_map[num] = i


"""
'Why can't we sort first and use two pointers?'
We would lose their original indices
"""
