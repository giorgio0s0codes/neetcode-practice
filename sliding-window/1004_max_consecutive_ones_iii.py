"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Approach:
    TODO

Time:  O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))                          # 6
    print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # 10
    print(s.longestOnes([0, 0, 0], 0))                                                  # 0
