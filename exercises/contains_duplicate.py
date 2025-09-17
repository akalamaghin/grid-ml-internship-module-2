from typing import List
import unittest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for num in nums:
            if num not in counts.keys():
                counts[num] = 1
            else:
                counts[num] += 1
                if counts[num] >= 2:
                    return True
        
        return False
    

class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.containsDuplicate([1, 2, 3, 1]), True)

    def test2(self):
        self.assertEqual(self.sol.containsDuplicate([1, 2, 3, 4]), False)

    def test3(self):
        self.assertEqual(self.sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == '__main__':
    unittest.main()
