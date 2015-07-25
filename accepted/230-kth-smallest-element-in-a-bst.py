# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        cur = root
        stack = []
        
        while None != cur.left:
            stack.append(cur)
            cur = cur.left
        
        for i in xrange(k - 1):
            if len(stack) > 0:
                stack[-1].left = cur.right
            
            if None != cur.right:
                cur = cur.right
            else:
                cur = stack.pop()
                
            while None != cur.left:
                stack.append(cur)
                cur = cur.left
        
        return cur.val
