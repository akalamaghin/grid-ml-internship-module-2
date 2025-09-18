import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letters = self.getLetters(s)
        t_letters = self.getLetters(t)

        if len(s_letters.keys()) != len(t_letters.keys()):
            return False
        
        return s_letters == t_letters

    def getLetters(self, s: str) -> dict:
        letters = {}

        for letter in s:
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 0

        return letters 


class SolutionTest(unittest.TestCase):
    sol = Solution()
    
    def test1(self):
        ans = self.sol.isAnagram("anagram", "nagaram")
        self.assertEqual(ans, True)

    def test2(self):
        ans = self.sol.isAnagram("rat", "car")
        self.assertEqual(ans, False)


if __name__ == '__main__':
    unittest.main()
