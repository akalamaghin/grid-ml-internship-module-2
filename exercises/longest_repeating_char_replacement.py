import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        window_freqs = {
            s[l]: 1
        }
        max_freq = 1

        while r < len(s) and l < len(s):
            window_freqs[s[r]] = window_freqs.get(s[r], 0) + 1

            max_window_freq = -1
            for _, val in window_freqs.items():
                max_window_freq = max(max_window_freq, val)
            
            window_size = r - l + 1
            change_cnt = window_size - max_window_freq

            if change_cnt > k:
                window_freqs[s[l]] -= 1
                l += 1
            else:
                max_freq = max_window_freq + change_cnt
            
            r += 1

        return max_freq


class SolutionTest(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(
            self.sol.characterReplacement("ABAB", 2),
            4
        )

    def test2(self):
        self.assertEqual(
            self.sol.characterReplacement("AABABBA", 1),
            4
        )


if __name__ == '__main__':
    unittest.main()
