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


"""
'Can you do this in one pass instead of 2 while loops?'
Yes, using a swap method.
"""


def moveZeroesOnePass(self, nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
