# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def real_flatten(self, node):
        if None == node or (None == node.left and None == node.right):
            return node
        
        cur = node
        right_head = node.right
        left = self.real_flatten(node.left)
        right = self.real_flatten(node.right)
        
        if None != node.left:
            node.right = node.left
            node.left = None
            cur = left
        if None != right_head:
            cur.right = right_head
            cur = right
        
        return cur
        
    def flatten(self, root):
        self.real_flatten(root)
