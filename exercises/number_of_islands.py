import unittest
from typing import List
from collections import deque


CONN_DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        islands_num = 0

        def bfs(start_i: int, start_j: int):
            queue = deque([(start_i, start_j)])
            grid[start_i][start_j] = "0"
            while queue:
                i, j = queue.popleft()
                for dir in CONN_DIRS:
                    vi, vj = i + dir[0], j + dir[1]
                    if 0 <= vi < n and 0 <= vj < m and grid[vi][vj] == "1":
                        queue.append((vi, vj))
                        grid[vi][vj] = "0"

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands_num += 1
                    bfs(i, j)

        return islands_num


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 1)

    def test2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 3)


if __name__ == '__main__':
    unittest.main()
