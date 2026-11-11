"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Approach:
    Sliding window that holds at most k zeros. Grow it to the right; when
    it has too many zeros, shrink it from the left until it is valid again.

Time:  O(n)  (each index enters and leaves the window once)
Space: O(1)
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zero = 0
        left = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length


if __name__ == "__main__":
    s = Solution()
    print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))                          # 6
    print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # 10
    print(s.longestOnes([0, 0, 0], 0))                                                  # 0
