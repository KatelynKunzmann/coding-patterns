from typing import List

""" Leetcode problem 167: Two Sum II - Input Array Is Sorted  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Time: O(n)
Space: O(1)
"""


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []


"""
'How would you solve if the input array was not sorted?'
I would use a hashmap to keep track of seen numbers. I would iterate through the input array the same way.

'Instead of returning only one solution, return all pairs that sum to the target.'
I would add those pairs to a list and return that list after parsing through the input array.
If you want to avoid duplicate pairs, then I would also add a check right after incrementing the left pointer
(or decrementing right pointer - only needed for one pointer). The check would be something like:
left += 1
while left < right and numbers[left] == numbers[left-1]:
    left += 1

'How would you handle streaming data or an array too large to fit in memory?' 
I would use a hash set (we could store the hash set on disk if needed) to store already seen numbers as the data is streamed in or to look at 
only a portion of the large array. I would check if the number has a complement in our set that 
sums to our target, if not then add it to the set and continue. 
"""
