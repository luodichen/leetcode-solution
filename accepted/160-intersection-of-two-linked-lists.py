# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if None == headA or None == headB:
            return None
        
        endA = headA
        lenA = 1
        while None != endA.next:
            endA = endA.next
            lenA += 1
        
        endB = headB
        lenB = 1
        while None != endB.next:
            endB = endB.next
            lenB += 1
            
        if endA != endB:
            return None
            
        curA = headA
        curB = headB
        
        if lenA > lenB:
            offset = lenA - lenB
            while offset > 0:
                curA = curA.next
                offset -= 1
        else:
            offset = lenB - lenA
            while offset > 0:
                curB = curB.next
                offset -= 1
        
        while curA != curB:
            curA = curA.next
            curB = curB.next
        
        return curA
