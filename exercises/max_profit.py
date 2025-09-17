from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit
    

class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test2(self):
        self.assertEqual(self.sol.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == '__main__':
    unittest.main()
