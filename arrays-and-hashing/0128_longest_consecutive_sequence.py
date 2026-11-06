"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Approach:
    Put every number in a set. Only start counting from numbers that begin
    a sequence (num - 1 not in the set), then walk up while num + i exists.

Time:  O(n)  (each number is visited by at most one walk)
Space: O(n)
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        longest = 0

        for num in count:
            i = 0
            if (num - 1) in count:
                continue
            while (num + i) in count:
                i += 1
                if longest < i:
                    longest = i
        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))              # 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))      # 9
    print(s.longestConsecutive([1, 0, 1, 2]))                        # 3
    print(s.longestConsecutive([]))                                  # 0
