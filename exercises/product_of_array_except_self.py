import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_products = [1 for _ in range(n)]
        suffix_products = [1 for _ in range(n)]
        products = [1 for _ in range(n)]

        for i in range(1, n):
            prefix_products[i] = nums[i - 1] * prefix_products[i - 1]

        for i in range(n - 2, -1, -1):
            suffix_products[i] = nums[i + 1] * suffix_products[i + 1]

        for i in range(n):
            products[i] = prefix_products[i] * suffix_products[i]

        return products
    

class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test2(self):
        self.assertEqual(self.sol.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


if __name__ == '__main__':
    unittest.main()
