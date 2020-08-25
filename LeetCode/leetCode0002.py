"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, prevSum = 0) -> ListNode:
        val = l1.val + l2.val + prevSum
        prevSum = val // 10
        result = ListNode(val % 10)
        if (l1.next is not None or l2.next is not None or prevSum != 0):
            if (l1.next is None):
                l1.next = ListNode()
            if (l2.next is None):
                l2.next = ListNode()
            result.next = self.addTwoNumbers(l1.next, l2.next, prevSum)
        
        return result