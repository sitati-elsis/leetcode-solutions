# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        if not l1:
            return l2
        carry = 0
        head = ListNode(None)
        result = head
        while l1 or l2:
            total = carry
            if l1:
                total = total + l1.val
                l1 = l1.next
            if l2:
                total = total + l2.val
                l2 = l2.next
            node = ListNode(total % 10)
            carry = total // 10
            result.next = node
            result = result.next
        if carry:
            node = ListNode(carry)
            result.next = node
        return head.next