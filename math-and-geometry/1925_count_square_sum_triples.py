"""
1925. Count Square Sum Triples
https://leetcode.com/problems/count-square-sum-triples/

Approach:
    <one or two lines on the idea>

Time:  O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def countTriples(self, n: int) -> int:
        squares = {i * i for i in range(1, n + 1)}
        count = 0

        for a in range(3, n+1):
            for b in range(3, n+1):
                total = (a*a) + (b*b)
                if total in squares:
                    count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countTriples(5))   # 2
    print(s.countTriples(10))  # 4
