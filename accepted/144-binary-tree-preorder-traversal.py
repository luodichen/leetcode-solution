# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):  
        ret = []
        stack = [root]
        
        while len(stack) > 0:
            node = stack.pop()
            if None == node:
                continue
            
            ret.append(node.val)
            
            if None != node.right:
                stack.append(node.right)
            if None != node.left:
                stack.append(node.left)
        
        return ret
