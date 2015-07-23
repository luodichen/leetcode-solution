# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, node):
        if node == None:
            return 0
        
        left = self.find(node.left)
        right = self.find(node.right)
        return (left if left > right else right) + 1
        
    
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        return self.find(root)
