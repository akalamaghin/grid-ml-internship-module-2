import unittest
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        return (
            self.hasPathSum(root.left, targetSum - root.val)
            or self.hasPathSum(root.right, targetSum - root.val)
        )


class SolutionTest(unittest.TestCase): 
    sol = Solution()

    def build_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values:
            return None
        
        nodes = [TreeNode(v) if v is not None else None for v in values]

        child_index = 1
        for _, node in enumerate(nodes):
            if node is not None:
                if child_index < len(nodes):
                    node.left = nodes[child_index]
                if child_index + 1 < len(nodes):
                    node.right = nodes[child_index + 1]
                child_index += 2
        
        return nodes[0]
    
    def test1(self):
        root = self.build_tree(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        )
        self.assertTrue(self.sol.hasPathSum(root, 22))

    def test2(self):
        root = self.build_tree([1, 2, 3])
        self.assertFalse(self.sol.hasPathSum(root, 5))

    def test3(self):
        root = self.build_tree([])
        self.assertTrue(self, self.sol.hasPathSum(root, 0))


if __name__ == '__main__':
    unittest.main()
