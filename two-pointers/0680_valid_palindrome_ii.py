"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/

Approach:
    Walk two pointers inward while the characters match. On the first
    mismatch we may delete one character, so check whether skipping the left
    one or the right one leaves a palindrome.

Time:  O(n)
Space: O(n)  (the slices copy up to n characters)
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                futuro_a = s[left+1:right+1]
                futuro_b = s[left:right]
                return futuro_a == futuro_a[::-1] or futuro_b == futuro_b[::-1]

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("aba"))   # True
    print(s.validPalindrome("abca"))  # True
    print(s.validPalindrome("abc"))   # False
