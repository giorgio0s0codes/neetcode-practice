"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Approach:
    Variable-size sliding window. Grow the window by moving right and adding
    nums[right]. While the sum is >= target, record the window length, then
    shrink from the left to look for a shorter valid window.

Time:  O(n)  (left and right each move at most n steps)
Space: O(1)
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)
                window_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0
        else:
            return min_length


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))           # 2
    print(s.minSubArrayLen(4, [1, 4, 4]))                    # 1
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))    # 0
