from typing import List

""" Leetcode Problem 128: Longest Consecutive Sequence https://leetcode.com/problems/longest-consecutive-sequence/
Time: O(n)
    - Building the set: O(n)
    - Outer loop: runs once for each unique number → O(n)
    - Inner while: crucially, each number can only be visited once across all iterations (since we only start sequences at the “smallest number” and expand forward).
        → This makes the total inner-loop work O(n) OVER THE WHOLE RUN, not O(n²).
    O(n) + O(n) => O(n)
Space: O(n)
"""


def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    longest_chain = 0
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 not in nums_set:
            curr_num = num
            curr_chain = 1
            while curr_num + 1 in nums_set:
                curr_num += 1
                curr_chain += 1
            longest_chain = max(longest_chain, curr_chain)
    return longest_chain


"""
'What if the input contains negative numbers?'
The algorithm already handles negative numbers.

'Can you modify your solution to also return the actual sequence, not just the length?'
See below
Time: O(n)
Space: O(n)
"""


def longestConsecutiveSequence(self, nums: List[int]) -> List[int]:
    if not nums:
        return 0
    longest_chain = 0
    longest_seq = []
    curr_seq = []
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 not in nums_set:
            curr_num = num
            curr_seq = [curr_num]

            while curr_num + 1 in nums_set:
                curr_num += 1
                curr_seq.append(curr_num)

            if len(curr_seq) > longest_chain:
                longest_chain = len(curr_seq)
                longest_seq = curr_seq
    return longest_seq


"""
'What if the array is already sorted or you can't use extra space?'
See below
Time: O(n⋅logn)
Space: O(1)

We return max(longest, current) in case we are at the end of the array - the else statement would not be entered
"""


def longestConsecutiveSorted(nums: List[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    longest = 1
    current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        elif nums[i] == (nums[i - 1] + 1):
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)
