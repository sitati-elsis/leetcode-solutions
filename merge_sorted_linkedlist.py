# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(None)
        head = result
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                result.next = node
                result = result.next
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                result.next = node
                result = result.next
                l2 = l2.next
        while l1:
            node = ListNode(l1.val)
            result.next = node
            result = result.next
            l1 = l1.next
        while l2:
            node = ListNode(l2.val)
            result.next = node
            result = result.next
            l2 = l2.next
        return head.next
        