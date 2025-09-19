import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        node = self
        seen = set()
        while node and id(node) not in seen:
            vals.append(str(node.val))
            seen.add(id(node))
            node = node.next
        if node:
            vals.append("...")
        return "->".join(vals)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr_node = head
        while curr_node is not None:
            if curr_node in visited:
                return True
            visited.add(curr_node)
            curr_node = curr_node.next
        return False


class SolutionTest(unittest.TestCase):
    sol = Solution()
    
    def list_to_nodes(self, lst, pos=-1):
        if not lst:
            return None
        nodes = [ListNode(val) for val in lst]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    def test1(self):
        head = self.list_to_nodes([3, 2, 0, -4], pos=1)
        self.assertTrue(self.sol.hasCycle(head))

    def test2(self):
        head = self.list_to_nodes([1, 2], pos=0)
        self.assertTrue(self.sol.hasCycle(head))

    def test3(self):
        head = self.list_to_nodes([1], pos=-1)
        self.assertFalse(self.sol.hasCycle(head))


if __name__ == "__main__":
    unittest.main()
