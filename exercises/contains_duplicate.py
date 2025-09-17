from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for num in nums:
            if num not in counts.keys():
                counts[num] = 1
            else:
                counts[num] += 1
                if counts[num] >= 2:
                    return True
        
        return False
    

if __name__ == '__main__':
    sol = Solution()

    test1 = [1, 2, 3, 2]
    test2 = [1, 2, 3, 4]

    print(f"{test1} contains duplcates - {sol.containsDuplicate(test1)}")
    print(f"{test2} contains duplcates - {sol.containsDuplicate(test2)}")
