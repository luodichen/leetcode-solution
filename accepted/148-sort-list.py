# https://leetcode.com/problems/sort-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        prev = None
        
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        
        root = ListNode(0)
        root.next = None
        cur = root
        
        while left is not None or right is not None:
            if left is None or (right is not None and right.val < left.val):
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            
            cur = cur.next
            cur.next = None
        
        return root.next
