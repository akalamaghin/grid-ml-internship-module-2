from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == '__main__':
    sol = Solution()

    nums = [3, 2, 4]
    target = 6

    indices = sol.twoSum(nums, target)
    print(
        f"nums={nums}, target={target}:\n"
        f"nums[{indices[0]}] + nums[{indices[1]}] = target"
    )
