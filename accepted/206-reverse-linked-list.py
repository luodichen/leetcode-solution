# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if None == head or None == head.next:
            return head
        
        cur = head
        prev = None
        next = head.next
        
        while None != cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev
