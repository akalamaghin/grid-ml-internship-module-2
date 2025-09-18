import unittest
from collections import deque


PARENTHESES_PAIRS = {
    '{': '}',
    '(': ')',
    '[': ']' 
}


class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()

        for par in s:
            if par in PARENTHESES_PAIRS.keys():
                dq.append(par)
            else:
                l_par = dq.pop()
                if par == PARENTHESES_PAIRS[l_par]:
                    continue
                else:
                    return False
                
        return len(dq) == 0


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.isValid("()"), True)

    def test2(self):
        self.assertEqual(self.sol.isValid("()[]{}"), True)

    def test3(self):
        self.assertEqual(self.sol.isValid("(]"), False)

    def test4(self):
        self.assertEqual(self.sol.isValid("([])"), True)

    def test5(self):
        self.assertEqual(self.sol.isValid("([)]"), False)


if __name__ == '__main__':
    unittest.main()
