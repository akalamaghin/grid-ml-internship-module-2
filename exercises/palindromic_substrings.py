import unittest


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        is_substr_palidrome = [[False for _ in range(n)] for _ in range(n)]
        
        for k in range(n):
            i, j = k, k

            while i >= 0 and j < n and s[i] == s[j]:
                is_substr_palidrome[i][j] = True
                i -= 1
                j += 1

            i, j = k, k + 1
            while i >= 0 and j < n and s[i] == s[j]:
                is_substr_palidrome[i][j] = True
                i -= 1
                j += 1

        pal_cnt = 0
        for l in is_substr_palidrome:
            for is_pal in l:
                if is_pal:
                    pal_cnt += 1

        return pal_cnt


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.countSubstrings("abc"), 3)

    def test2(self):
        self.assertEqual(self.sol.countSubstrings("aaa"), 6)


if __name__ == '__main__':
    unittest.main()
