# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def find(self, node, depth):
        if None == node.left and None == node.right:
            return depth
        elif None == node.left:
            return self.find(node.right, depth + 1)
        elif None == node.right:
            return self.find(node.left, depth + 1)
        else:
            left = self.find(node.left, depth + 1)
            right = self.find(node.right, depth + 1)
            return left if left < right else right
        
    def minDepth(self, root):
        if None == root:
            return 0
        else:
            return self.find(root, 1)
