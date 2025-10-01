from typing import List

""" Leetcode problem 11: Container With Most Water https://leetcode.com/problems/container-with-most-water/
Time: O(n)
Space: O(1)
"""


def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(curr_area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
