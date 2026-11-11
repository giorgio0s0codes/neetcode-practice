"""
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string s and an integer k, return the length of the longest
substring of s that contains at most k distinct characters.

Approach:
    TODO

Time:  O(?)
Space: O(?)
"""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s:str, k: int) -> int:
        count = defaultdict(int)
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            count[char] += 1
            while len(count) > k:
                left_char = s[left]
                count[left_char] -= 1
                if count[left_char] == 0:
                    del count[left_char]
                left += 1
            max_length = max(max_length, (right - left + 1))
        return max_length



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstringKDistinct("eceba", 2))   # 3  ("ece")
    print(s.lengthOfLongestSubstringKDistinct("aa", 1))      # 2  ("aa")
    print(s.lengthOfLongestSubstringKDistinct("abaccc", 2))  # 4  ("accc")
    print(s.lengthOfLongestSubstringKDistinct("abc", 0))     # 0
