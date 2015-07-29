# https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if None == head:
            return
        
        cur = head
        stack = []
        
        while None != cur:
            stack.append(cur)
            cur = cur.next
        
        cur = head
        stack.pop(0)
        
        while len(stack) > 0:
            cur.next = stack.pop()
            cur = cur.next
            
            if (len(stack) > 0):
                cur.next = stack.pop(0)
                cur = cur.next
        
        cur.next = None
