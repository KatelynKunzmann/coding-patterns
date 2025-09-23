""" Leetcode Problem 31: Next Permutation https://leetcode.com/problems/next-permutation/
1) Find the pivot - find the first place starting from the right where the order increases
2) Find the swap partner - find the smallest number that is > pivot
3) Swap them (with tuple unpacking) then reverse the rest of the list
Time: O(n)
Space: O(1)
"""

def next_permutation(nums: List[int]) -> None
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i < 0:
        nums.reverse()
        return

    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    
    nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])