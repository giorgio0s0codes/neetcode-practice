"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Approach:
    One pointer at each end. Skip anything that isn't a letter or digit,
    then compare the two characters ignoring case and move both inward.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(s.isPalindrome("race a car"))                      # False
    print(s.isPalindrome(" "))                               # True
    print(s.isPalindrome("0P"))                              # False
