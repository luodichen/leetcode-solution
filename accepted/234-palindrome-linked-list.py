# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if None == head:
            return True
        
        if None == head.next:
            return True
            
        point = head
        point2x = head
        
        ne = point.next
        prev = None
        
        back = None
        forward = None
        while None != point2x.next:
            if None == point2x.next.next:
                back = point
                forward = point.next
                back.next = prev
                ne = forward
                break
            
            point2x = point2x.next.next
            point.next = prev
            
            prev = point
            point = ne
            ne = point.next
            
        if None == back:
            back = prev
            forward = point.next
            ne = point
            
        ret = True
        while None != forward:
            if back.val != forward.val:
                ret = False
            
            forward = forward.next
            prev = back.next
            back.next = ne
            ne = back
            back = prev
        
        return ret
