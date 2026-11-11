"""
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

Approach:
    Variable-size sliding window holding at most 2 distinct fruit types.
    Count each type in the window. While there are more than 2 types, shrink
    from the left, removing a type once its count hits 0. Track the longest
    window seen.

Time:  O(n)  (left and right each move at most n steps)
Space: O(1)  (at most 3 keys in the dict)
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


if __name__ == "__main__":
    s = Solution()
    print(s.totalFruit([1, 2, 1]))              # 3
    print(s.totalFruit([0, 1, 2, 2]))           # 3
    print(s.totalFruit([1, 2, 3, 2, 2]))        # 4
