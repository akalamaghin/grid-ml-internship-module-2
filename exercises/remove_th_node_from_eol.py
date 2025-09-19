from typing import Optional
import unittest


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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        reversed_head = self.reverseList(head)

        curr, prev = reversed_head, None
        for _ in range(n - 1):
            assert curr is not None
            prev, curr = curr, curr.next

        if prev is None:
            reversed_head = curr.next if curr else None
        else:
            prev.next = curr.next if curr else None

        return self.reverseList(reversed_head)


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

    def test_example1(self):
        head = self.list_to_nodes([1, 2, 3, 4, 5])
        res = self.sol.removeNthFromEnd(head, 2)
        self.assertEqual(self.nodes_to_list(res), [1, 2, 3, 5])

    def test_example2(self):
        head = self.list_to_nodes([1])
        res = self.sol.removeNthFromEnd(head, 1)
        self.assertEqual(self.nodes_to_list(res), [])

    def test_example3(self):
        head = self.list_to_nodes([1, 2])
        res = self.sol.removeNthFromEnd(head, 1)
        self.assertEqual(self.nodes_to_list(res), [1])


if __name__ == "__main__":
    unittest.main()
