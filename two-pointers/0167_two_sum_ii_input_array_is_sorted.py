"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Approach:
    The array is sorted, so start one pointer at each end. If the sum is too
    big, move right inward to make it smaller; if too small, move left
    inward to make it bigger. Return 1-indexed positions.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            suma_actual = numbers[left] + numbers[right]
            if suma_actual == target:
                return [left + 1, right + 1]
            elif suma_actual > target:
                right -= 1
            else:
                left += 1


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(s.twoSum([2, 3, 4], 6))       # [1, 3]
    print(s.twoSum([-1, 0], -1))        # [1, 2]
