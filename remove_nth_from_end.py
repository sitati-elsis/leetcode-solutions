# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        prev = None
        count = 1
        while count <= n - 1:
            fast = fast.next
            count = count + 1
        while fast.next:
            prev = slow
            fast = fast.next
            slow = slow.next
        if prev:
            prev.next = slow.next
            del slow
            return head
        else:
            return slow.next
            