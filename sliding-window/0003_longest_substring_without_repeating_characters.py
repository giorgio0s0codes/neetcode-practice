"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
    TODO

Time:  O(?)
Space: O(?)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in word:
                word.remove(s[left])
                left += 1
            word.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))    # 3
    print(s.lengthOfLongestSubstring("bbbbb"))       # 1
    print(s.lengthOfLongestSubstring("pwwkew"))      # 3
    print(s.lengthOfLongestSubstring(""))            # 0
