# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def __init__(self):
        self.result = True
        
    def treeHeight(self, node):
        if not self.result:
            return 0
        if None == node:
            return 0
        
        left = self.treeHeight(node.left)
        right = self.treeHeight(node.right)
        
        if left - right > 1 or left - right < -1:
            self.result = False
        
        return 1 + (left if left > right else right)
        
    def isBalanced(self, root):
        self.result = True
        self.treeHeight(root)
        return self.result
