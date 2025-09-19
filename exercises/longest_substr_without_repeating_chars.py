import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, r = 0, 0
        last_window_char_occ = {
            s[l]: 0
        }
        max_window_size = r - l + 1

        while r < len(s) - 1:
            r += 1
            if s[r] in last_window_char_occ.keys():
                l = last_window_char_occ[s[r]] + 1
                last_window_char_occ = {
                    key: val for key, val in last_window_char_occ.items() if val >= l
                }

            last_window_char_occ[s[r]] = r
            max_window_size = max(max_window_size, r - l + 1)

        return max_window_size
    

class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(
            self.sol.lengthOfLongestSubstring("abcabcbb"),
            3
        )

    def test2(self):
        self.assertEqual(
            self.sol.lengthOfLongestSubstring("bbbbb"),
            1
        )

    def test3(self):
        self.assertEqual(
            self.sol.lengthOfLongestSubstring("pwwkew"),
            3
        )


if __name__ == '__main__':
    unittest.main()
