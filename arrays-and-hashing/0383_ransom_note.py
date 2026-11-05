"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Approach:
    Count the letters in magazine, then spend one for each letter of
    ransomNote. If a letter is missing or used up, it can't be built.

Time:  O(m + n)
Space: O(1)  (at most 26 lowercase letters)
"""

from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts = {}

        for char in magazine:
            counts[char] = counts.get(char, 0) + 1
        for char in ransomNote:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))      # False
    print(s.canConstruct("aa", "ab"))    # False
    print(s.canConstruct("aa", "aab"))   # True
    print(s.canConstruct("", "abc"))     # True
