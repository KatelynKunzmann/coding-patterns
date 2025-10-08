from typing import List

""" Leetcode Problem 15: 3Sum https://leetcode.com/problems/3sum/
Skip dupes twice - at the first value and the pointer we advance
Only need to skip dupes on the side we advance (left side here)
Since it is sorted, this is why it works
Time: O(n^2)
Space: O(1)
"""


def threeSum(self, nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
        return []
    nums.sort()
    triplets = []
    for i, num in enumerate(nums):
        if num > 0:
            break
        if i > 0 and num == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            threesum = num + nums[left] + nums[right]
            if threesum == 0:
                triplets.append([num, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif threesum < 0:
                left += 1
            else:
                right -= 1
    return triplets


"""
"Why is sorting necessary?"
Efficient two-pointer scan: left/right movement depends on order
Avoiding duplicates: easy to skip repeated values by comparing with previous elements
Without sorting, you’d need a more complicated set/hash-based approach → slower
-------------------------------------------
“How would you handle 4-sum, 5-sum, or k-sum?”
Recursively reduce k-sum to 2-sum using a helper:
Sort the array
For each number, recursively call (k-1)-sum on the rest of the array
Base case: 2-sum solved with two pointers
Complexity grows: O(n^(k-1))
---------------------------------------------
Edge cases:
Array with all zeros → expect [[0,0,0]]
Array with less than 3 elements → return []
Array with no triplets summing to zero → return []
Array with very large numbers → check integer overflow (Python handles this automatically)
"""
