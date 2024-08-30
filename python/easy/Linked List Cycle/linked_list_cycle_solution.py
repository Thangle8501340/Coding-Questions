# Definition for singly-linked list.
from typing import Optional
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # hasCycle - check if the linked list input has a cycle within it's list
    # input - head: Optional[ListNode] = the head of the linked list
    # output - bool: True if the linked list has a cycle, false if otherwise
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    def test_hasCycle(self):
        solution = Solution()
        
        # Table of test cases
        test_cases = [
            {"input": ([3, 2, 0, -4], 1), "expected": True},
            {"input": ([1, 2], 0), "expected": True},
            {"input": ([1], -1), "expected": False},
            {"input": ([1, 2, 3, 4], -1), "expected": False},
            {"input": ([], -1), "expected": False},
            {"input": ([1], 0), "expected": True},
            {"input": ([1], -1), "expected": False},
        ]
        
        for case in test_cases:
            values, pos = case["input"]
            with self.subTest(case=case):
                head = self.create_linked_list_with_cycle(values, pos)
                self.assertEqual(solution.hasCycle(head), case["expected"])

if __name__ == '__main__':
    unittest.main()