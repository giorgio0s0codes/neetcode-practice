"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Approach:
    Start with the widest container (one pointer at each end). The shorter
    wall limits the water, so move that pointer inward: moving the taller
    one can never give a bigger area.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = h * w
            water = max(water, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return water


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(s.maxArea([1, 1]))                       # 1
    print(s.maxArea([4, 3, 2, 1, 4]))              # 16
