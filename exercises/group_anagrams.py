import unittest
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s))
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(
            self.sol.groupAnagrams(sorted(["eat", "tea", "tan", "ate", "nat", "bat"])),
            sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
        )

    def test2(self):
        self.assertEqual(self.sol.groupAnagrams([""]), [[""]])

    def test3(self):
        self.assertEqual(self.sol.groupAnagrams(["a"]), [["a"]])


if __name__ == '__main__':
    unittest.main()
