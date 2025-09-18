import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        running_sum = max_sum + 0
        
        for num in nums[1:]:
            running_sum = max(running_sum + num, num)
            max_sum = max(max_sum, running_sum)

            if running_sum < 0:
                running_sum = 0

        return max_sum


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        ans = self.sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(ans, 6)

    def test2(self):
        ans = self.sol.maxSubArray([1])
        self.assertEqual(ans, 1)

    def test3(self):
        ans = self.sol.maxSubArray([5, 4, -1, 7, 8])
        self.assertEqual(ans, 23)

    def test4(self):
        ans = self.sol.maxSubArray([-2, 1])
        self.assertEqual(ans, 1)


if __name__ == '__main__':
    unittest.main()
