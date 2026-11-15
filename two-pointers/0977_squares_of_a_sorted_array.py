"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Approach:
    The input is sorted, so the largest square is always at one of the two
    ends (a big negative squares to a big number). Compare the squares at
    both ends and place the larger one at the back of the result, moving
    that pointer inward. Fill the result from right to left.

Time:  O(n)
Space: O(n)  (the result array)
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        resultado = [0] * n
        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            l_square = nums[left] * nums[left]
            r_square = nums[right] * nums[right]

            if l_square > r_square:
                resultado[i] = l_square
                left += 1
            else:
                resultado[i] = r_square
                right -= 1

        return resultado


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))      # [0, 1, 9, 16, 100]
    print(s.sortedSquares([-7, -3, 2, 3, 11]))      # [4, 9, 9, 49, 121]a
