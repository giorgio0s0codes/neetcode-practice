"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

Approach:
    Fixed-size sliding window. Sum the first k numbers, then slide one step
    at a time: add the new number on the right and drop the one that left
    on the left. Track the max sum and divide by k once at the end.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))   # 12.75
    print(s.findMaxAverage([5], 1))                      # 5.0
    print(s.findMaxAverage([-1, -2, -3], 2))             # -1.5
