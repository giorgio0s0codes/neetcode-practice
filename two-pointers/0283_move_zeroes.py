"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Approach:
    Keep a writer pointer at the next slot for a non-zero value. Scan with a
    reader pointer; every time it finds a non-zero, swap it into the writer
    slot and advance the writer. Zeros end up pushed to the back and the
    relative order of the non-zeros is preserved.

Time:  O(n)
Space: O(1)  (in-place)
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writer = 0

        for reader in range(len(nums)):
            if nums[reader] != 0:
                nums[writer], nums[reader] = nums[reader], nums[writer]
                writer += 1


if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]
    s.moveZeroes(a)
    print(a)  # [1, 3, 12, 0, 0]

    b = [0]
    s.moveZeroes(b)
    print(b)  # [0]
