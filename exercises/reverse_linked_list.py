import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next
        return self is None and other is None

    def __repr__(self):
        vals = []
        node = self
        while node:
            vals.append(str(node.val))
            node = node.next
        return "->".join(vals)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = [head]
        next_ = head.next
        while next_ is not None:
            nodes.append(next_)
            next_ = next_.next

        nodes.reverse()
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]


class SolutionTest(unittest.TestCase):
    sol = Solution()
    
    def list_to_nodes(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def nodes_to_list(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def test1(self):
        head = self.list_to_nodes([1, 2, 3, 4, 5])
        reversed_head = self.sol.reverseList(head)
        self.assertEqual(self.nodes_to_list(reversed_head), [5, 4, 3, 2, 1])

    def test2(self):
        head = self.list_to_nodes([1, 2])
        reversed_head = self.sol.reverseList(head)
        self.assertEqual(self.nodes_to_list(reversed_head), [2, 1])

    def test3(self):
        head = self.list_to_nodes([])
        reversed_head = self.sol.reverseList(head)
        self.assertEqual(self.nodes_to_list(reversed_head), [])


if __name__ == "__main__":
    unittest.main()
