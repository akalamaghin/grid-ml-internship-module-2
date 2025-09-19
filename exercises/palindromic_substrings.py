import unittest


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        pal_cnt = 0
        for k in range(n):
            i, j = k, k

            while i >= 0 and j < n and s[i] == s[j]:
                pal_cnt += 1
                i -= 1
                j += 1

            i, j = k, k + 1
            while i >= 0 and j < n and s[i] == s[j]:
                pal_cnt += 1
                i -= 1
                j += 1

        return pal_cnt


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.countSubstrings("abc"), 3)

    def test2(self):
        self.assertEqual(self.sol.countSubstrings("aaa"), 6)


if __name__ == '__main__':
    unittest.main()
