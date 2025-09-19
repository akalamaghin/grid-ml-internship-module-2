from typing import Optional, List, Dict
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        nodevals_by_depth = {}

        assert root is not None
        self.traverse(root, nodevals_by_depth)

        for depth, nodevals in nodevals_by_depth.items():
            if depth == 0:
                continue

            mid = len(nodevals) // 2
            first_half = nodevals[:mid]
            second_half = nodevals[-mid:]

            if first_half != second_half[::-1]:
                return False
            
        return True

    def traverse(
        self,
        root: Optional[TreeNode],
        nodevals_by_depth: Dict[int, List[int | None]],
        depth: int = 0
    ):
        if depth not in nodevals_by_depth.keys():
            nodevals_by_depth[depth] = [root.val if root is not None else None]
        else:
            nodevals_by_depth[depth].append(root.val if root is not None else None)

        if root is not None:
            self.traverse(root.left, nodevals_by_depth, depth+1)
            self.traverse(root.right, nodevals_by_depth, depth+1)

        return

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
        root = self.build_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(self.sol.isSymmetric(root))

    def test2(self):
        root = self.build_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(self.sol.isSymmetric(root))


if __name__ == '__main__':
    unittest.main()
