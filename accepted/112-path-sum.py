# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def found(self, node, sum, target):
        if node == None:
            return False
        elif node.left == None and node.right == None:
            return sum + node.val == target
        elif self.found(node.left, sum + node.val, target):
            return True
        else:
            return self.found(node.right, sum + node.val, target)
    
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        return self.found(root, 0, sum)
