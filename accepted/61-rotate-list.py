# https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if None == head:
            return None
        if 0 == k:
            return head
        
        list_len = 1
        last = head
        
        while None != last.next:
            last = last.next
            list_len += 1
        
        k = k % list_len
        if 0 == k:
            return head
        
        prev = None
        new_head = head
        
        for i in xrange(list_len - k):
            prev = new_head
            new_head = new_head.next
        
        prev.next = None
        last.next = head
        
        return new_head
