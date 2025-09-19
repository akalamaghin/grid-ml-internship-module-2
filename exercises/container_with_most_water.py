import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = -1
        l, r = 0, len(height) - 1
    
        while l < r:
            amount = (r - l) * min(height[l], height[r])
            max_amount = max(max_amount, amount)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_amount


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(
            self.sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]),
            49
        )
    
    def test2(self):
        self.assertEqual(self.sol.maxArea([1, 1]), 1)


if __name__ == '__main__':
    unittest.main()
