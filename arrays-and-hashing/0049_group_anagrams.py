"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Approach:
    Anagrams share the same sorted string, so use it as a dict key and
    group the original words under it.

Time:  O(n * k log k)  (n words, k = longest word)
Space: O(n * k)
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            anagram_map[key].append(string)
        return list(anagram_map.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["eat","tea","ate"],["tan","nat"],["bat"]]
    print(s.groupAnagrams([""]))   # [[""]]
    print(s.groupAnagrams(["a"]))  # [["a"]]
