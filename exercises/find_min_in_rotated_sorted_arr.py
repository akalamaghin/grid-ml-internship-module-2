import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(
            self.solution.findMin([3, 4, 5, 1, 2]), 1
        )

    def test2(self):
        self.assertEqual(
            self.solution.findMin([4, 5, 6, 7, 0, 1, 2]), 0
        )

    def test3(self):
        self.assertEqual(
            self.solution.findMin([11, 13, 15, 17]), 11
        )


if __name__ == "__main__":
    unittest.main()
