from typing import List, Optional
import unittest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: (x[0], x[1]))
        new_intervals = [intervals[0]]

        for current in intervals[1:]:
            last = new_intervals[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                new_intervals.append(current)

        return new_intervals


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(
            self.sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]]
        )

    def test2(self):
        self.assertEqual(
            self.sol.merge([[1, 4], [4, 5]]),
            [[1, 5]]
        )

    def test3(self):
        self.assertEqual(
            self.sol.merge([[4, 7], [1, 4]]),
            [[1, 7]]
        )


if __name__ == '__main__':
    unittest.main()
