from typing import List

"""Leetcode Problem 283: Move Zeroes https://leetcode.com/problems/move-zeroes/
Time: O(n)
Space: O(1)
"""


def moveZeroes(self, nums: List[int]) -> None:
    shift = 0
    search = 0
    while search < len(nums):
        if nums[search] != 0:
            nums[shift] = nums[search]
            shift += 1
        search += 1
    while shift < len(nums):
        nums[shift] = 0
        shift += 1
